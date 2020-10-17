from cloudshell.shell.standards.core.resource_config_entities import (
    GenericResourceConfig,
    PasswordAttrRO,
    ResourceAttrRO,
    ResourceBoolAttrRO,
    ResourceListAttrRO,
)


class VCenterResourceConfig(GenericResourceConfig):
    user = ResourceAttrRO("User", ResourceAttrRO.NAMESPACE.SHELL_NAME)

    password = PasswordAttrRO("Password", PasswordAttrRO.NAMESPACE.SHELL_NAME)

    default_dv_switch = ResourceAttrRO(
        "Default dvSwitch", ResourceAttrRO.NAMESPACE.SHELL_NAME
    )

    holding_network = ResourceAttrRO(
        "Holding Network", ResourceAttrRO.NAMESPACE.SHELL_NAME
    )

    vm_cluster = ResourceAttrRO("VM Cluster", ResourceAttrRO.NAMESPACE.SHELL_NAME)

    vm_resource_pool = ResourceAttrRO(
        "VM Resource Pool", ResourceAttrRO.NAMESPACE.SHELL_NAME
    )

    vm_storage = ResourceAttrRO("VM Storage", ResourceAttrRO.NAMESPACE.SHELL_NAME)

    saved_sandbox_storage = ResourceAttrRO(
        "Saved Sandbox Storage", ResourceAttrRO.NAMESPACE.SHELL_NAME
    )

    behavior_during_save = ResourceAttrRO(
        "Behavior during save", ResourceAttrRO.NAMESPACE.SHELL_NAME
    )

    vm_location = ResourceAttrRO("VM Location", ResourceAttrRO.NAMESPACE.SHELL_NAME)

    shutdown_method = ResourceAttrRO(
        "Shutdown Method", ResourceAttrRO.NAMESPACE.SHELL_NAME
    )

    ovf_tool_path = ResourceAttrRO("OVF Tool Path", ResourceAttrRO.NAMESPACE.SHELL_NAME)

    reserved_networks = ResourceListAttrRO(
        "Reserved Networks", ResourceListAttrRO.NAMESPACE.SHELL_NAME
    )

    execution_server_selector = ResourceAttrRO(
        "Execution Server Selector", ResourceAttrRO.NAMESPACE.SHELL_NAME
    )

    promiscuous_mode = ResourceBoolAttrRO(
        "Promiscuous Mode", ResourceBoolAttrRO.NAMESPACE.SHELL_NAME
    )
