import importlib
import pkgutil
from typing import Dict, Any
import typer

def register_tools(app: typer.Typer, tools_package_path: str, tools_package_name: str):
    """
    Dynamically discovers and registers subcommands from the tools package.
    Supports nested categories (folders) and modules.
    """
    import os
    package = importlib.import_module(tools_package_name)
    base_dir = os.path.dirname(package.__file__)
    
    category_apps = {}

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                module_rel_name = rel_path.replace(os.path.sep, ".").replace(".py", "")
                full_module_name = f"{tools_package_name}.{module_rel_name}"
                
                try:
                    module = importlib.import_module(full_module_name)
                except Exception:
                    continue
                
                if hasattr(module, "app"):
                    parts = module_rel_name.split('.')
                    if len(parts) > 1:
                        category = parts[0]
                        if category not in category_apps:
                            cat_app = typer.Typer(help=f"🛠️ {category.capitalize()} tools.")
                            category_apps[category] = cat_app
                            app.add_typer(cat_app, name=category)
                        
                        # Add tool to category
                        category_apps[category].add_typer(module.app, name=parts[-1].replace("_", "-"))
                    else:
                        # Top level
                        app.add_typer(module.app, name=module_rel_name.replace("_", "-"))
