# Ecovacs Model Override

A minimal Home Assistant custom integration that applies a generic hardware
model override to `deebot-client`.

## What it does

`deebot-client` selects a static capability profile from the cloud-reported
hardware class of a robot. When a class is associated with the wrong profile,
this integration substitutes one configured class with another existing profile
before the lookup takes place. The substitution already verified for the
installed device is kept unchanged in this release.

- Only the configured hardware class is affected; every other class keeps its
  original behaviour.
- No platforms, entities, services or config flow are added.
- The override targets both `deebot_client.hardware.get_static_device_info` and
  `deebot_client.api_client.get_static_device_info`, and is applied at import time.
- No user-configurable options are exposed in this release.

This repository contains only the mapping. It does not contain Quick Commands or
cleaning-scene functionality.

## Compatibility

- Home Assistant 2026.11+
- `deebot-client==18.7.0` (pinned in `manifest.json` because the override targets
  two internal functions of that release)
- Works with the stock Home Assistant Ecovacs integration and with the separate
  [Ecovacs Custom Cleaning Scenes](https://github.com/nino76/ha-ecovacs-cleaning-scenes)
  integration. The two projects use different
  domains (`ecovacs_model_override` and `ecovacs`) and can be installed together.
  The scenes integration declares `after_dependencies` so it is set up after this
  integration when both are installed and this one is configured.

## Installation (Home Assistant Marketplace)

1. In Home Assistant open **Settings → Devices & services → Marketplace** (the three-dot menu).
2. Add `https://github.com/nino76/ecovacs-model-override` as a **Custom repository** with category **Integration**.
3. Install **Ecovacs Model Override**.
4. Add this line to `configuration.yaml`:

   ```yaml
   ecovacs_model_override:
   ```

5. Restart Home Assistant.

The YAML entry is required: it makes Home Assistant load the override module at
bootstrap, before Ecovacs config entries initialise their devices. It creates no
entity and has no options.

Manual install: copy `custom_components/ecovacs_model_override/` into
`<config>/custom_components/`, add the YAML line above and restart.

## Usage

Nothing to configure. After a restart, the configured hardware class is resolved
with the replacement static capability profile. If you also use saved cleaning
scenes, install the separate Quick Commands repository; no additional step is
needed here.

## Troubleshooting

- Override not applied: check that `ecovacs_model_override:` is present in
  `configuration.yaml` and that Home Assistant has been restarted.
- After a `deebot-client` upgrade the override may stop matching. Keep the pinned
  version until compatibility has been confirmed.

## Credits

Repository: https://github.com/nino76/ecovacs-model-override

Author: nino76

Based on the Home Assistant core Ecovacs integration and the `deebot-client` library.

## License

MIT — see `LICENSE`.
