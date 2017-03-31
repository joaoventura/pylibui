import ctypes

class __libui_control_struct(ctypes.Structure):
    """Wrapper for the C struct."""
    pass

c_func_type_int_structp_voidp = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.POINTER(__libui_control_struct),
    ctypes.c_void_p)
c_func_type_void_structp_voidp = ctypes.CFUNCTYPE(
    None,
    ctypes.POINTER(__libui_control_struct),
    ctypes.c_void_p)
c_func_type_void_structp_structp_voidp = ctypes.CFUNCTYPE(
    None,
    ctypes.POINTER(__libui_control_struct),
    ctypes.POINTER(__libui_control_struct),
    ctypes.c_void_p)
c_func_type_int_voidp = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.c_void_p)
c_func_type_void_voidp = ctypes.CFUNCTYPE(
    None,
    ctypes.c_void_p)

def get_c_callback_func_ptr(func, c_type):
    c_callback = c_type(func)

    c_handle_ptr = ctypes.cast(c_callback, ctypes.c_void_p).value

    return c_handle_ptr
