import typer
from pytoolkit.main import app
from pytoolkit.core.registry import register_tools

def test_registry_discovery():
    # Verify that tools are registered
    # This assumes we have at least one tool in src/pytoolkit/tools/
    commands = [cmd.name for cmd in app.registered_commands]
    # In our current setup, register_tools is called in main.py
    # and it adds sub-typer apps, not direct commands to the root app's registered_commands list
    # Typer sub-apps are in app.registered_groups
    groups = [group.name for group in app.registered_groups]
    
    assert "sys-info" in groups
    assert "network" in groups
    assert "crypto" in groups
    assert "format" in groups

def test_version_callback():
    from pytoolkit.main import version_callback
    import pytest
    
    with pytest.raises(typer.Exit):
        version_callback(True)
