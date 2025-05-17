from ableton.v2.base import liveobj_valid
from ableton.v3.live import is_device_rack


def flatten_active_device_chain(track_or_chain):
    devices = []
    chain_devices = track_or_chain.devices if liveobj_valid(track_or_chain) else []
    for device in chain_devices:
        devices.append(device)
        devices.extend(flatten_active_device_chain(active_chain(device)))

    return devices

def active_chain(device):
    if is_device_rack(device) and device.view.is_showing_chain_devices and device.is_active:
        return device.view.selected_chain
