


def __init_plugin__(app=None):    
    from pymol import cmd
    

    from .pymol_interface import pocket
    cmd.extend('pocket', pocket)
