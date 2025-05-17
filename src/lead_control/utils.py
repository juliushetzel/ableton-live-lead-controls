from ableton.v2.base import liveobj_valid
from ableton.v3.live import is_device_rack


def flatten_active_device_chain(track_or_chain):
    devices = []
    chain_devices = track_or_chain.devices if liveobj_valid(track_or_chain) else []
    for device in chain_devices:
        if device.is_active:
            devices.append(device)
            if is_device_rack(device):
                child_chains = device.chains or []
                devices.extend(flatten_chains(child_chains))
    return devices


def flatten_chains(chains):
    devices = []
    for chain in chains:
        devices.extend(flatten_active_device_chain(chain))
    return devices


