import importlib
import pkgutil
from typing import Dict, Any
import typer

def register_tools(app: typer.Typer, tools_package_path: str, tools_package_name: str):
    """
    Dynamically discovers and registers subcommands from the tools package.
    Each module in the tools package should expose a 'app' or 'tool_app' variable.
    """
    package = importlib.import_module(tools_package_name)
    
    for loader, module_name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_module_name = f"{tools_package_name}.{module_name}"
        module = importlib.import_module(full_module_name)
        
        # Check if the module has a 'app' (Typer instance)
        if hasattr(module, "app") and isinstance(module.app, typer.Typer):
            # Use the module name as the subcommand name unless specified
            command_name = getattr(module, "COMMAND_NAME", module_name.replace("_", "-"))
            app.add_typer(module.app, name=command_name)
        # Or if it's a single command function decorated with @app.command() in its own app
        # Typer handles this via add_typer if it's a Typer instance
