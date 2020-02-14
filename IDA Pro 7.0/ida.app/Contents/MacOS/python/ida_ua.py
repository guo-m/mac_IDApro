# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: ua
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_ua', [dirname(__file__)])
        except ImportError:
            import _ida_ua
            return _ida_ua
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_ua', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_ua = swig_import_helper()
    del swig_import_helper
else:
    import _ida_ua
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


import ida_idaapi

import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        func.func_dict["bc695redef"] = True
        return func

class operands_array(object):
    """
    Proxy of C++ wrapped_array_t<(op_t,8)> class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    data = _swig_property(_ida_ua.operands_array_data_get)
    def __init__(self, *args):
        """
        __init__(self, data) -> operands_array
        """
        this = _ida_ua.new_operands_array(*args)
        try: self.this.append(this)
        except: self.this = this
    def __len__(self, *args):
        """
        __len__(self) -> size_t
        """
        return _ida_ua.operands_array___len__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, i) -> op_t
        """
        return _ida_ua.operands_array___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, i, v)
        """
        return _ida_ua.operands_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_ua.delete_operands_array
    __del__ = lambda self : None;
operands_array_swigregister = _ida_ua.operands_array_swigregister
operands_array_swigregister(operands_array)

class op_t(object):
    """
    Proxy of C++ op_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    n = _swig_property(_ida_ua.op_t_n_get, _ida_ua.op_t_n_set)
    type = _swig_property(_ida_ua.op_t_type_get, _ida_ua.op_t_type_set)
    offb = _swig_property(_ida_ua.op_t_offb_get, _ida_ua.op_t_offb_set)
    offo = _swig_property(_ida_ua.op_t_offo_get, _ida_ua.op_t_offo_set)
    flags = _swig_property(_ida_ua.op_t_flags_get, _ida_ua.op_t_flags_set)
    def set_shown(self, *args):
        """
        set_shown(self)
        """
        return _ida_ua.op_t_set_shown(self, *args)

    def clr_shown(self, *args):
        """
        clr_shown(self)
        """
        return _ida_ua.op_t_clr_shown(self, *args)

    def shown(self, *args):
        """
        shown(self) -> bool
        """
        return _ida_ua.op_t_shown(self, *args)

    dtype = _swig_property(_ida_ua.op_t_dtype_get, _ida_ua.op_t_dtype_set)
    def is_reg(self, *args):
        """
        is_reg(self, r) -> bool
        """
        return _ida_ua.op_t_is_reg(self, *args)

    def is_imm(self, *args):
        """
        is_imm(self, v) -> bool
        """
        return _ida_ua.op_t_is_imm(self, *args)

    specflag1 = _swig_property(_ida_ua.op_t_specflag1_get, _ida_ua.op_t_specflag1_set)
    specflag2 = _swig_property(_ida_ua.op_t_specflag2_get, _ida_ua.op_t_specflag2_set)
    specflag3 = _swig_property(_ida_ua.op_t_specflag3_get, _ida_ua.op_t_specflag3_set)
    specflag4 = _swig_property(_ida_ua.op_t_specflag4_get, _ida_ua.op_t_specflag4_set)
    def __get_reg_phrase__(self, *args):
        """
        __get_reg_phrase__(self) -> uint16
        """
        return _ida_ua.op_t___get_reg_phrase__(self, *args)

    def __set_reg_phrase__(self, *args):
        """
        __set_reg_phrase__(self, r)
        """
        return _ida_ua.op_t___set_reg_phrase__(self, *args)

    def __get_value__(self, *args):
        """
        __get_value__(self) -> ea_t
        """
        return _ida_ua.op_t___get_value__(self, *args)

    def __set_value__(self, *args):
        """
        __set_value__(self, v)
        """
        return _ida_ua.op_t___set_value__(self, *args)

    def __get_addr__(self, *args):
        """
        __get_addr__(self) -> ea_t
        """
        return _ida_ua.op_t___get_addr__(self, *args)

    def __set_addr__(self, *args):
        """
        __set_addr__(self, v)
        """
        return _ida_ua.op_t___set_addr__(self, *args)

    def __get_specval__(self, *args):
        """
        __get_specval__(self) -> ea_t
        """
        return _ida_ua.op_t___get_specval__(self, *args)

    def __set_specval__(self, *args):
        """
        __set_specval__(self, v)
        """
        return _ida_ua.op_t___set_specval__(self, *args)

    def assign(self, *args):
        """
        assign(self, other)
        """
        return _ida_ua.op_t_assign(self, *args)

    def has_reg(self, r):
        """
        Checks if the operand accesses the given processor register
        """
        return self.reg == r.reg

    reg = property(__get_reg_phrase__, __set_reg_phrase__)
    phrase = property(__get_reg_phrase__, __set_reg_phrase__)
    value = property(__get_value__, __set_value__)
    addr = property(__get_addr__, __set_addr__)
    specval = property(__get_specval__, __set_specval__)

    def __init__(self, *args):
        """
        __init__(self) -> op_t
        """
        this = _ida_ua.new_op_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_ua.delete_op_t
    __del__ = lambda self : None;
op_t_swigregister = _ida_ua.op_t_swigregister
op_t_swigregister(op_t)
cvar = _ida_ua.cvar
o_void = cvar.o_void
o_reg = cvar.o_reg
o_mem = cvar.o_mem
o_phrase = cvar.o_phrase
o_displ = cvar.o_displ
o_imm = cvar.o_imm
o_far = cvar.o_far
o_near = cvar.o_near
o_idpspec0 = cvar.o_idpspec0
o_idpspec1 = cvar.o_idpspec1
o_idpspec2 = cvar.o_idpspec2
o_idpspec3 = cvar.o_idpspec3
o_idpspec4 = cvar.o_idpspec4
o_idpspec5 = cvar.o_idpspec5
OF_NO_BASE_DISP = _ida_ua.OF_NO_BASE_DISP
OF_OUTER_DISP = _ida_ua.OF_OUTER_DISP
PACK_FORM_DEF = _ida_ua.PACK_FORM_DEF
OF_NUMBER = _ida_ua.OF_NUMBER
OF_SHOW = _ida_ua.OF_SHOW
dt_byte = _ida_ua.dt_byte
dt_word = _ida_ua.dt_word
dt_dword = _ida_ua.dt_dword
dt_float = _ida_ua.dt_float
dt_double = _ida_ua.dt_double
dt_tbyte = _ida_ua.dt_tbyte
dt_packreal = _ida_ua.dt_packreal
dt_qword = _ida_ua.dt_qword
dt_byte16 = _ida_ua.dt_byte16
dt_code = _ida_ua.dt_code
dt_void = _ida_ua.dt_void
dt_fword = _ida_ua.dt_fword
dt_bitfild = _ida_ua.dt_bitfild
dt_string = _ida_ua.dt_string
dt_unicode = _ida_ua.dt_unicode
dt_ldbl = _ida_ua.dt_ldbl
dt_byte32 = _ida_ua.dt_byte32
dt_byte64 = _ida_ua.dt_byte64


def insn_add_cref(*args):
  """
  insn_add_cref(insn, to, opoff, type)
  """
  return _ida_ua.insn_add_cref(*args)

def insn_add_dref(*args):
  """
  insn_add_dref(insn, to, opoff, type)
  """
  return _ida_ua.insn_add_dref(*args)

def insn_add_off_drefs(*args):
  """
  insn_add_off_drefs(insn, x, type, outf) -> ea_t
  """
  return _ida_ua.insn_add_off_drefs(*args)

def insn_create_stkvar(*args):
  """
  insn_create_stkvar(insn, x, v, flags) -> bool
  """
  return _ida_ua.insn_create_stkvar(*args)
class insn_t(object):
    """
    Proxy of C++ insn_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args):
        """
        __init__(self) -> insn_t
        """
        this = _ida_ua.new_insn_t(*args)
        try: self.this.append(this)
        except: self.this = this
    cs = _swig_property(_ida_ua.insn_t_cs_get, _ida_ua.insn_t_cs_set)
    ip = _swig_property(_ida_ua.insn_t_ip_get, _ida_ua.insn_t_ip_set)
    ea = _swig_property(_ida_ua.insn_t_ea_get, _ida_ua.insn_t_ea_set)
    itype = _swig_property(_ida_ua.insn_t_itype_get, _ida_ua.insn_t_itype_set)
    def is_canon_insn(self, *args):
        """
        is_canon_insn(self) -> bool
        """
        return _ida_ua.insn_t_is_canon_insn(self, *args)

    def get_canon_feature(self, *args):
        """
        get_canon_feature(self) -> uint32
        """
        return _ida_ua.insn_t_get_canon_feature(self, *args)

    def get_canon_mnem(self, *args):
        """
        get_canon_mnem(self) -> char const *
        """
        return _ida_ua.insn_t_get_canon_mnem(self, *args)

    size = _swig_property(_ida_ua.insn_t_size_get, _ida_ua.insn_t_size_set)
    segpref = _swig_property(_ida_ua.insn_t_segpref_get, _ida_ua.insn_t_segpref_set)
    insnpref = _swig_property(_ida_ua.insn_t_insnpref_get, _ida_ua.insn_t_insnpref_set)
    flags = _swig_property(_ida_ua.insn_t_flags_get, _ida_ua.insn_t_flags_set)
    ops = _swig_property(_ida_ua.insn_t_ops_get, _ida_ua.insn_t_ops_set)
    def is_macro(self, *args):
        """
        is_macro(self) -> bool
        """
        return _ida_ua.insn_t_is_macro(self, *args)

    def get_next_byte(self, *args):
        """
        get_next_byte(self) -> uint8
        """
        return _ida_ua.insn_t_get_next_byte(self, *args)

    def get_next_word(self, *args):
        """
        get_next_word(self) -> uint16
        """
        return _ida_ua.insn_t_get_next_word(self, *args)

    def get_next_dword(self, *args):
        """
        get_next_dword(self) -> uint32
        """
        return _ida_ua.insn_t_get_next_dword(self, *args)

    def get_next_qword(self, *args):
        """
        get_next_qword(self) -> uint64
        """
        return _ida_ua.insn_t_get_next_qword(self, *args)

    def create_op_data(self, *args):
        """
        create_op_data(self, ea_, opoff, dtype) -> bool
        create_op_data(self, ea_, op) -> bool
        """
        return _ida_ua.insn_t_create_op_data(self, *args)

    def create_stkvar(self, *args):
        """
        create_stkvar(self, x, v, flags_) -> bool
        """
        return _ida_ua.insn_t_create_stkvar(self, *args)

    def add_cref(self, *args):
        """
        add_cref(self, to, opoff, type)
        """
        return _ida_ua.insn_t_add_cref(self, *args)

    def add_dref(self, *args):
        """
        add_dref(self, to, opoff, type)
        """
        return _ida_ua.insn_t_add_dref(self, *args)

    def add_off_drefs(self, *args):
        """
        add_off_drefs(self, x, type, outf) -> ea_t
        """
        return _ida_ua.insn_t_add_off_drefs(self, *args)

    def __get_ops__(self, *args):
        """
        __get_ops__(self) -> operands_array
        """
        return _ida_ua.insn_t___get_ops__(self, *args)

    def __get_operand__(self, *args):
        """
        __get_operand__(self, n) -> op_t
        """
        return _ida_ua.insn_t___get_operand__(self, *args)

    def __get_auxpref__(self, *args):
        """
        __get_auxpref__(self) -> uint16
        """
        return _ida_ua.insn_t___get_auxpref__(self, *args)

    def __set_auxpref__(self, *args):
        """
        __set_auxpref__(self, v)
        """
        return _ida_ua.insn_t___set_auxpref__(self, *args)

    def assign(self, *args):
        """
        assign(self, other)
        """
        return _ida_ua.insn_t_assign(self, *args)

    ops = property(__get_ops__)

    if _BC695:
        Operands = ops

    Op1 = property(lambda self: self.__get_operand__(0))
    Op2 = property(lambda self: self.__get_operand__(1))
    Op3 = property(lambda self: self.__get_operand__(2))
    Op4 = property(lambda self: self.__get_operand__(3))
    Op5 = property(lambda self: self.__get_operand__(4))
    Op6 = property(lambda self: self.__get_operand__(5))

    auxpref = property(__get_auxpref__, __set_auxpref__)

    def __iter__(self):
        return (self.ops[idx] for idx in xrange(0, 8))

    def __getitem__(self, idx):
        """
        Operands can be accessed directly as indexes
        @return op_t: Returns an operand of type op_t
        """
        if idx >= 8:
            raise KeyError
        else:
            return self.ops[idx]

    __swig_destroy__ = _ida_ua.delete_insn_t
    __del__ = lambda self : None;
insn_t_swigregister = _ida_ua.insn_t_swigregister
insn_t_swigregister(insn_t)
INSN_MACRO = _ida_ua.INSN_MACRO
INSN_MODMAC = _ida_ua.INSN_MODMAC
STKVAR_VALID_SIZE = _ida_ua.STKVAR_VALID_SIZE


def get_lookback(*args):
  """
  get_lookback() -> int
  """
  return _ida_ua.get_lookback(*args)

def calc_dataseg(*args):
  """
  calc_dataseg(insn, n=-1, rgnum=-1) -> ea_t
  """
  return _ida_ua.calc_dataseg(*args)

def map_data_ea(*args):
  """
    map_data_ea(insn, addr, opnum=-1) -> ea_t
    map_data_ea(insn, op) -> ea_t
    """
  return _ida_ua.map_data_ea(*args)

def map_code_ea(*args):
  """
    map_code_ea(insn, addr, opnum) -> ea_t
    map_code_ea(insn, op) -> ea_t
    """
  return _ida_ua.map_code_ea(*args)

def map_ea(*args):
  """
    map_ea(insn, op, iscode) -> ea_t
    map_ea(insn, addr, opnum, iscode) -> ea_t
    """
  return _ida_ua.map_ea(*args)
class outctx_base_t(object):
    """
    Proxy of C++ outctx_base_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    insn_ea = _swig_property(_ida_ua.outctx_base_t_insn_ea_get, _ida_ua.outctx_base_t_insn_ea_set)
    outbuf = _swig_property(_ida_ua.outctx_base_t_outbuf_get, _ida_ua.outctx_base_t_outbuf_set)
    default_lnnum = _swig_property(_ida_ua.outctx_base_t_default_lnnum_get, _ida_ua.outctx_base_t_default_lnnum_set)
    def only_main_line(self, *args):
        """
        only_main_line(self) -> bool
        """
        return _ida_ua.outctx_base_t_only_main_line(self, *args)

    def multiline(self, *args):
        """
        multiline(self) -> bool
        """
        return _ida_ua.outctx_base_t_multiline(self, *args)

    def force_code(self, *args):
        """
        force_code(self) -> bool
        """
        return _ida_ua.outctx_base_t_force_code(self, *args)

    def stack_view(self, *args):
        """
        stack_view(self) -> bool
        """
        return _ida_ua.outctx_base_t_stack_view(self, *args)

    def display_voids(self, *args):
        """
        display_voids(self) -> bool
        """
        return _ida_ua.outctx_base_t_display_voids(self, *args)

    def set_gen_xrefs(self, *args):
        """
        set_gen_xrefs(self, on=True)
        """
        return _ida_ua.outctx_base_t_set_gen_xrefs(self, *args)

    def set_gen_cmt(self, *args):
        """
        set_gen_cmt(self, on=True)
        """
        return _ida_ua.outctx_base_t_set_gen_cmt(self, *args)

    def clr_gen_label(self, *args):
        """
        clr_gen_label(self)
        """
        return _ida_ua.outctx_base_t_clr_gen_label(self, *args)

    def set_gen_label(self, *args):
        """
        set_gen_label(self)
        """
        return _ida_ua.outctx_base_t_set_gen_label(self, *args)

    def set_gen_demangled_label(self, *args):
        """
        set_gen_demangled_label(self)
        """
        return _ida_ua.outctx_base_t_set_gen_demangled_label(self, *args)

    def set_comment_addr(self, *args):
        """
        set_comment_addr(self, ea)
        """
        return _ida_ua.outctx_base_t_set_comment_addr(self, *args)

    def print_label_now(self, *args):
        """
        print_label_now(self) -> bool
        """
        return _ida_ua.outctx_base_t_print_label_now(self, *args)

    def forbid_annotations(self, *args):
        """
        forbid_annotations(self) -> int
        """
        return _ida_ua.outctx_base_t_forbid_annotations(self, *args)

    def restore_ctxflags(self, *args):
        """
        restore_ctxflags(self, saved_flags)
        """
        return _ida_ua.outctx_base_t_restore_ctxflags(self, *args)

    def out_printf(self, *args):
        """
        out_printf(self, format)
        """
        return _ida_ua.outctx_base_t_out_printf(self, *args)

    def out_value(self, *args):
        """
        out_value(self, x, outf=0) -> flags_t
        """
        return _ida_ua.outctx_base_t_out_value(self, *args)

    def out_symbol(self, *args):
        """
        out_symbol(self, c)
        """
        return _ida_ua.outctx_base_t_out_symbol(self, *args)

    def out_chars(self, *args):
        """
        out_chars(self, c, n)
        """
        return _ida_ua.outctx_base_t_out_chars(self, *args)

    def out_spaces(self, *args):
        """
        out_spaces(self, len)
        """
        return _ida_ua.outctx_base_t_out_spaces(self, *args)

    def out_line(self, *args):
        """
        out_line(self, str, color=0)
        """
        return _ida_ua.outctx_base_t_out_line(self, *args)

    def out_keyword(self, *args):
        """
        out_keyword(self, str)
        """
        return _ida_ua.outctx_base_t_out_keyword(self, *args)

    def out_register(self, *args):
        """
        out_register(self, str)
        """
        return _ida_ua.outctx_base_t_out_register(self, *args)

    def out_tagon(self, *args):
        """
        out_tagon(self, tag)
        """
        return _ida_ua.outctx_base_t_out_tagon(self, *args)

    def out_tagoff(self, *args):
        """
        out_tagoff(self, tag)
        """
        return _ida_ua.outctx_base_t_out_tagoff(self, *args)

    def out_addr_tag(self, *args):
        """
        out_addr_tag(self, ea)
        """
        return _ida_ua.outctx_base_t_out_addr_tag(self, *args)

    def out_colored_register_line(self, *args):
        """
        out_colored_register_line(self, str)
        """
        return _ida_ua.outctx_base_t_out_colored_register_line(self, *args)

    def out_char(self, *args):
        """
        out_char(self, c)
        """
        return _ida_ua.outctx_base_t_out_char(self, *args)

    def out_btoa(self, *args):
        """
        out_btoa(self, Word, radix=0)
        """
        return _ida_ua.outctx_base_t_out_btoa(self, *args)

    def out_long(self, *args):
        """
        out_long(self, v, radix)
        """
        return _ida_ua.outctx_base_t_out_long(self, *args)

    def out_name_expr(self, *args):
        """
        out_name_expr(self, x, ea, off=BADADDR) -> bool
        """
        return _ida_ua.outctx_base_t_out_name_expr(self, *args)

    def close_comment(self, *args):
        """
        close_comment(self)
        """
        return _ida_ua.outctx_base_t_close_comment(self, *args)

    def flush_outbuf(self, *args):
        """
        flush_outbuf(self, indent=-1) -> bool
        """
        return _ida_ua.outctx_base_t_flush_outbuf(self, *args)

    def flush_buf(self, *args):
        """
        flush_buf(self, buf, indent=-1) -> bool
        """
        return _ida_ua.outctx_base_t_flush_buf(self, *args)

    def term_outctx(self, *args):
        """
        term_outctx(self, prefix=None) -> int
        """
        return _ida_ua.outctx_base_t_term_outctx(self, *args)

    def gen_printf(self, *args):
        """
        gen_printf(self, indent, format) -> bool
        """
        return _ida_ua.outctx_base_t_gen_printf(self, *args)

    def gen_empty_line(self, *args):
        """
        gen_empty_line(self) -> bool
        """
        return _ida_ua.outctx_base_t_gen_empty_line(self, *args)

    def gen_border_line(self, *args):
        """
        gen_border_line(self, solid=False) -> bool
        """
        return _ida_ua.outctx_base_t_gen_border_line(self, *args)

    def gen_cmt_line(self, *args):
        """
        gen_cmt_line(self, format) -> bool
        """
        return _ida_ua.outctx_base_t_gen_cmt_line(self, *args)

    def gen_collapsed_line(self, *args):
        """
        gen_collapsed_line(self, format) -> bool
        """
        return _ida_ua.outctx_base_t_gen_collapsed_line(self, *args)

    def gen_block_cmt(self, *args):
        """
        gen_block_cmt(self, cmt, color) -> bool
        """
        return _ida_ua.outctx_base_t_gen_block_cmt(self, *args)

    def setup_outctx(self, *args):
        """
        setup_outctx(self, prefix, makeline_flags)
        """
        return _ida_ua.outctx_base_t_setup_outctx(self, *args)

    def retrieve_cmt(self, *args):
        """
        retrieve_cmt(self) -> ssize_t
        """
        return _ida_ua.outctx_base_t_retrieve_cmt(self, *args)

    def retrieve_name(self, *args):
        """
        retrieve_name(self, arg2, arg3) -> ssize_t
        """
        return _ida_ua.outctx_base_t_retrieve_name(self, *args)

    def gen_xref_lines(self, *args):
        """
        gen_xref_lines(self) -> bool
        """
        return _ida_ua.outctx_base_t_gen_xref_lines(self, *args)

    def init_lines_array(self, *args):
        """
        init_lines_array(self, answers, maxsize)
        """
        return _ida_ua.outctx_base_t_init_lines_array(self, *args)

    def get_stkvar(self, *args):
        """
        get_stkvar(self, arg2, arg3, arg4, arg5) -> member_t *
        """
        return _ida_ua.outctx_base_t_get_stkvar(self, *args)

    def gen_empty_line_without_annotations(self, *args):
        """
        gen_empty_line_without_annotations(self)
        """
        return _ida_ua.outctx_base_t_gen_empty_line_without_annotations(self, *args)

outctx_base_t_swigregister = _ida_ua.outctx_base_t_swigregister
outctx_base_t_swigregister(outctx_base_t)
CTXF_MAIN = _ida_ua.CTXF_MAIN
CTXF_MULTI = _ida_ua.CTXF_MULTI
CTXF_CODE = _ida_ua.CTXF_CODE
CTXF_STACK = _ida_ua.CTXF_STACK
CTXF_GEN_XREFS = _ida_ua.CTXF_GEN_XREFS
CTXF_XREF_STATE = _ida_ua.CTXF_XREF_STATE
XREFSTATE_NONE = _ida_ua.XREFSTATE_NONE
XREFSTATE_GO = _ida_ua.XREFSTATE_GO
XREFSTATE_DONE = _ida_ua.XREFSTATE_DONE
CTXF_GEN_CMT = _ida_ua.CTXF_GEN_CMT
CTXF_CMT_STATE = _ida_ua.CTXF_CMT_STATE
COMMSTATE_NONE = _ida_ua.COMMSTATE_NONE
COMMSTATE_GO = _ida_ua.COMMSTATE_GO
COMMSTATE_DONE = _ida_ua.COMMSTATE_DONE
CTXF_VOIDS = _ida_ua.CTXF_VOIDS
CTXF_NORMAL_LABEL = _ida_ua.CTXF_NORMAL_LABEL
CTXF_DEMANGLED_LABEL = _ida_ua.CTXF_DEMANGLED_LABEL
CTXF_LABEL_OK = _ida_ua.CTXF_LABEL_OK
CTXF_DEMANGLED_OK = _ida_ua.CTXF_DEMANGLED_OK
OOF_SIGNMASK = _ida_ua.OOF_SIGNMASK
OOFS_IFSIGN = _ida_ua.OOFS_IFSIGN
OOFS_NOSIGN = _ida_ua.OOFS_NOSIGN
OOFS_NEEDSIGN = _ida_ua.OOFS_NEEDSIGN
OOF_SIGNED = _ida_ua.OOF_SIGNED
OOF_NUMBER = _ida_ua.OOF_NUMBER
OOF_WIDTHMASK = _ida_ua.OOF_WIDTHMASK
OOFW_IMM = _ida_ua.OOFW_IMM
OOFW_8 = _ida_ua.OOFW_8
OOFW_16 = _ida_ua.OOFW_16
OOFW_24 = _ida_ua.OOFW_24
OOFW_32 = _ida_ua.OOFW_32
OOFW_64 = _ida_ua.OOFW_64
OOF_ADDR = _ida_ua.OOF_ADDR
OOF_OUTER = _ida_ua.OOF_OUTER
OOF_ZSTROFF = _ida_ua.OOF_ZSTROFF
OOF_NOBNOT = _ida_ua.OOF_NOBNOT
OOF_SPACES = _ida_ua.OOF_SPACES
MAKELINE_NONE = _ida_ua.MAKELINE_NONE
MAKELINE_BINPREF = _ida_ua.MAKELINE_BINPREF
MAKELINE_VOID = _ida_ua.MAKELINE_VOID
MAKELINE_STACK = _ida_ua.MAKELINE_STACK

class outctx_t(outctx_base_t):
    """
    Proxy of C++ outctx_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    bin_ea = _swig_property(_ida_ua.outctx_t_bin_ea_get, _ida_ua.outctx_t_bin_ea_set)
    bin_state = _swig_property(_ida_ua.outctx_t_bin_state_get, _ida_ua.outctx_t_bin_state_set)
    gl_bpsize = _swig_property(_ida_ua.outctx_t_gl_bpsize_get, _ida_ua.outctx_t_gl_bpsize_set)
    bin_width = _swig_property(_ida_ua.outctx_t_bin_width_get, _ida_ua.outctx_t_bin_width_set)
    insn = _swig_property(_ida_ua.outctx_t_insn_get, _ida_ua.outctx_t_insn_set)
    curlabel = _swig_property(_ida_ua.outctx_t_curlabel_get, _ida_ua.outctx_t_curlabel_set)
    def setup_outctx(self, *args):
        """
        setup_outctx(self, prefix, flags)
        """
        return _ida_ua.outctx_t_setup_outctx(self, *args)

    def retrieve_cmt(self, *args):
        """
        retrieve_cmt(self) -> ssize_t
        """
        return _ida_ua.outctx_t_retrieve_cmt(self, *args)

    def retrieve_name(self, *args):
        """
        retrieve_name(self, arg2, arg3) -> ssize_t
        """
        return _ida_ua.outctx_t_retrieve_name(self, *args)

    def gen_xref_lines(self, *args):
        """
        gen_xref_lines(self) -> bool
        """
        return _ida_ua.outctx_t_gen_xref_lines(self, *args)

    def out_mnem(self, *args):
        """
        out_mnem(self, width=8, postfix=None)
        """
        return _ida_ua.outctx_t_out_mnem(self, *args)

    def out_custom_mnem(self, *args):
        """
        out_custom_mnem(self, mnem, width=8, postfix=None)
        """
        return _ida_ua.outctx_t_out_custom_mnem(self, *args)

    def out_mnemonic(self, *args):
        """
        out_mnemonic(self)
        """
        return _ida_ua.outctx_t_out_mnemonic(self, *args)

    def out_one_operand(self, *args):
        """
        out_one_operand(self, n) -> bool
        """
        return _ida_ua.outctx_t_out_one_operand(self, *args)

    def out_immchar_cmts(self, *args):
        """
        out_immchar_cmts(self)
        """
        return _ida_ua.outctx_t_out_immchar_cmts(self, *args)

    def gen_func_header(self, *args):
        """
        gen_func_header(self, pfn)
        """
        return _ida_ua.outctx_t_gen_func_header(self, *args)

    def gen_func_footer(self, *args):
        """
        gen_func_footer(self, pfn)
        """
        return _ida_ua.outctx_t_gen_func_footer(self, *args)

    def out_data(self, *args):
        """
        out_data(self, analyze_only)
        """
        return _ida_ua.outctx_t_out_data(self, *args)

    def out_specea(self, *args):
        """
        out_specea(self, segtype) -> bool
        """
        return _ida_ua.outctx_t_out_specea(self, *args)

    def gen_header_extra(self, *args):
        """
        gen_header_extra(self)
        """
        return _ida_ua.outctx_t_gen_header_extra(self, *args)

    def gen_header(self, *args):
        """
        gen_header(self, flags=((1 << 0)|(1 << 1)), proc_name=None, proc_flavour=None)
        """
        return _ida_ua.outctx_t_gen_header(self, *args)

outctx_t_swigregister = _ida_ua.outctx_t_swigregister
outctx_t_swigregister(outctx_t)
GH_PRINT_PROC = _ida_ua.GH_PRINT_PROC
GH_PRINT_ASM = _ida_ua.GH_PRINT_ASM
GH_PRINT_BYTESEX = _ida_ua.GH_PRINT_BYTESEX
GH_PRINT_HEADER = _ida_ua.GH_PRINT_HEADER
GH_BYTESEX_HAS_HIGHBYTE = _ida_ua.GH_BYTESEX_HAS_HIGHBYTE
GH_PRINT_PROC_AND_ASM = _ida_ua.GH_PRINT_PROC_AND_ASM
GH_PRINT_PROC_ASM_AND_BYTESEX = _ida_ua.GH_PRINT_PROC_ASM_AND_BYTESEX
GH_PRINT_ALL = _ida_ua.GH_PRINT_ALL
GH_PRINT_ALL_BUT_BYTESEX = _ida_ua.GH_PRINT_ALL_BUT_BYTESEX


def create_outctx(*args):
  """
  create_outctx(ea, F=0, suspop=0) -> outctx_base_t
  """
  return _ida_ua.create_outctx(*args)

def print_insn_mnem(*args):
  """
  print_insn_mnem(ea) -> bool
  """
  return _ida_ua.print_insn_mnem(*args)

def get_dtype_flag(*args):
  """
  get_dtype_flag(dtype) -> flags_t
  """
  return _ida_ua.get_dtype_flag(*args)

def get_dtype_size(*args):
  """
  get_dtype_size(dtype) -> size_t
  """
  return _ida_ua.get_dtype_size(*args)

def create_insn(*args):
  """
  create_insn(ea, out=None) -> int
  """
  return _ida_ua.create_insn(*args)

def decode_insn(*args):
  """
  decode_insn(out, ea) -> int
  """
  return _ida_ua.decode_insn(*args)

def can_decode(*args):
  """
  can_decode(ea) -> bool
  """
  return _ida_ua.can_decode(*args)

def print_operand(*args):
  """
  print_operand(ea, n, getn_flags=0, newtype=None) -> bool
  """
  return _ida_ua.print_operand(*args)

def decode_prev_insn(*args):
  """
  decode_prev_insn(out, ea) -> ea_t
  """
  return _ida_ua.decode_prev_insn(*args)

def guess_table_address(*args):
  """
  guess_table_address(insn) -> ea_t
  """
  return _ida_ua.guess_table_address(*args)

def guess_table_size(*args):
  """
  guess_table_size(insn, jump_table) -> asize_t
  """
  return _ida_ua.guess_table_size(*args)

def decode_preceding_insn(*args):
  """
  decode_preceding_insn(out, ea) -> PyObject *


  Decodes the preceding instruction. Please check ua.hpp / decode_preceding_insn()
  @param ea: current ea
  @param out: instruction storage
  @return: tuple(preceeding_ea or BADADDR, farref = Boolean)
  """
  return _ida_ua.decode_preceding_insn(*args)

def construct_macro(*args):
  """
  construct_macro(insn, enable, build_macro) -> bool


  See ua.hpp's construct_macro().
  """
  return _ida_ua.construct_macro(*args)

def get_dtype_by_size(*args):
  """
  get_dtype_by_size(size) -> int
  """
  return _ida_ua.get_dtype_by_size(*args)

def get_immvals(*args):
  """
  get_immvals(ea, n) -> PyObject *
  """
  return _ida_ua.get_immvals(*args)

def insn_t__from_ptrval__(*args):
  """
  insn_t__from_ptrval__(ptrval) -> insn_t
  """
  return _ida_ua.insn_t__from_ptrval__(*args)

def op_t__from_ptrval__(*args):
  """
  op_t__from_ptrval__(ptrval) -> op_t
  """
  return _ida_ua.op_t__from_ptrval__(*args)

def outctx_base_t__from_ptrval__(*args):
  """
  outctx_base_t__from_ptrval__(ptrval) -> outctx_base_t
  """
  return _ida_ua.outctx_base_t__from_ptrval__(*args)

def outctx_t__from_ptrval__(*args):
  """
  outctx_t__from_ptrval__(ptrval) -> outctx_t
  """
  return _ida_ua.outctx_t__from_ptrval__(*args)
#<pycode(py_ua)>
ua_mnem = print_insn_mnem
#</pycode(py_ua)>

if _BC695:
    import ida_idaapi
    @bc695redef
    def codeSeg(ea, opnum):
        insn = insn_t()
        if decode_insn(insn, ea):
            return _ida_ua.map_code_ea(insn, insn.ops[opnum])
        else:
            return ida_idaapi.BADADDR
    get_dtyp_by_size=get_dtype_by_size
    get_dtyp_flag=get_dtype_flag
    get_dtyp_size=get_dtype_size
    get_operand_immvals=get_immvals
    op_t.dtyp = op_t.dtype
    cmd = insn_t()
    @bc695redef
    def decode_insn(*args):
        if len(args) == 1:
            tmp = insn_t()
            rc = _ida_ua.decode_insn(tmp, args[0])
            cmd.assign(tmp)
            return rc
        else:
            return _ida_ua.decode_insn(*args)
    @bc695redef
    def create_insn(*args):
        if len(args) == 1:
            tmp = insn_t()
            rc = _ida_ua.create_insn(args[0], tmp)
            cmd.assign(tmp)
            return rc
        else:
            return _ida_ua.create_insn(*args)
    @bc695redef
    def decode_prev_insn(*args):
        if len(args) == 1:
            tmp = insn_t()
            rc = _ida_ua.decode_prev_insn(tmp, args[0])
            cmd.assign(tmp)
            return rc
        else:
            return _ida_ua.decode_prev_insn(*args)
    @bc695redef
    def decode_preceding_insn(*args):
        if len(args) == 1:
            tmp = insn_t()
            rc = _ida_ua.decode_preceding_insn(tmp, args[0])
            cmd.assign(tmp)
            return rc
        else:
            return _ida_ua.decode_preceding_insn(*args)
    import ida_ida
    UA_MAXOP=ida_ida.UA_MAXOP
    dt_3byte=dt_byte
    tbo_123=0
    tbo_132=0
    tbo_213=0
    tbo_231=0
    tbo_312=0
    tbo_321=0
    @bc695redef
    def ua_add_cref(opoff, to, rtype):
        return cmd.add_cref(to, opoff, rtype)
    @bc695redef
    def ua_add_dref(opoff, to, rtype):
        return cmd.add_dref(to, opoff, rtype)
    @bc695redef
    def ua_add_off_drefs(x, rtype):
        return cmd.add_off_drefs(x, rtype, 0)
    @bc695redef
    def ua_add_off_drefs2(x, rtype, outf):
        return cmd.add_off_drefs(x, rtype, outf)
    @bc695redef
    def ua_dodata(ea, dtype):
        return cmd.create_op_data(ea, 0, dtype)
    @bc695redef
    def ua_dodata2(opoff, ea, dtype):
        return cmd.create_op_data(ea, opoff, dtype)
    @bc695redef
    def ua_stkvar2(x, v, flags):
        return cmd.create_stkvar(x, v, flags)



