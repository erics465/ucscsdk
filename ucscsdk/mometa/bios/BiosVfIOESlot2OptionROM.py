"""This module contains the general information for BiosVfIOESlot2OptionROM ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfIOESlot2OptionROMConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_IOESLOT2_OPTION_ROM_DISABLED = "disabled"
    VP_IOESLOT2_OPTION_ROM_ENABLED = "enabled"
    VP_IOESLOT2_OPTION_ROM_LEGACY_ONLY = "legacy-only"
    VP_IOESLOT2_OPTION_ROM_PLATFORM_DEFAULT = "platform-default"
    VP_IOESLOT2_OPTION_ROM_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_IOESLOT2_OPTION_ROM_UEFI_ONLY = "uefi-only"


class BiosVfIOESlot2OptionROM(ManagedObject):
    """This is BiosVfIOESlot2OptionROM class."""

    consts = BiosVfIOESlot2OptionROMConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfIOESlot2OptionROM", "biosVfIOESlot2OptionROM", "IOESlot2-OptionROM", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], [u'biosVProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_ioe_slot2_option_rom": MoPropertyMeta("vp_ioe_slot2_option_rom", "vpIOESlot2OptionROM", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "legacy-only", "platform-default", "platform-recommended", "uefi-only"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpIOESlot2OptionROM": "vp_ioe_slot2_option_rom", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_ioe_slot2_option_rom = None

        ManagedObject.__init__(self, "BiosVfIOESlot2OptionROM", parent_mo_or_dn, **kwargs)

