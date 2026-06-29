# Ansible Collection AzerothCore

Deploys an [AzerothCore](https://www.azerothcore.org/) Docker environment using
the official `acore-docker` project. The collection automates cloning the
required repositories, building custom server images, deploying the Docker
Compose stack, and optionally custom modules ([Indvidiual Progression](https://github.com/ZhengPeiRu21/mod-individual-progression)
is included by default)

This project has no affiliation with AzerothCore.

## Features

* Clone the official `acore-docker` repository.
* Build custom AzerothCore server images from source.
* Build and optionally push images to a Docker registry.
* Deploy the Docker Compose stack.
* Mount custom modules and configuration.
* Support the Individual Progression module by default.
* Includes playbooks for common build and deployment workflows.

## Requirements

The target host should have:

* Docker
* Docker Compose
* Git
* Sufficient disk space for building AzerothCore images.

If image pushing is enabled, a Docker registry is also required. By default,
the collection assumes a registry is available on the Ansible control host on
port `5000`.

## Roles

### `azerothcore_install`

Prepares the AzerothCore Docker project. This role clones the upstream
`acore-docker` repository, creates the required directory structure, and writes
the generated Docker Compose configuration.

#### Variables

| Variable                                         | Description                                                       |
| ------------------------------------------------ | ----------------------------------------------------------------- |
| `azerothcore_install_path`                       | Docker Compose project directory.                                 |
| `azerothcore_install_modules_path`               | Directory containing AzerothCore modules.                         |
| `azerothcore_install_config_path`                | Server configuration directory.                                   |
| `azerothcore_install_assets_path`                | Client data directory.                                            |
| `azerothcore_install_phpmyadmin_port`            | Port where phpMyAdmin will be exposed.                            |
| `azerothcore_install_db_pwd`                     | MariaDB root password. **Required.**                              |
| `azerothcore_install_compose_repository`         | Upstream `acore-docker` repository.                               |
| `azerothcore_install_compose_repository_version` | Version/ref of the upstream repository.                           |
| `azerothcore_install_compose_repository_path`    | Path where `acore-docker` will be cloned.                         |
| `azerothcore_install_compose_overrides`          | Overrides applied to the generated runtime Compose configuration. |

### `azerothcore_modules`

Manages AzerothCore modules, including optional support for the Individual
Progression module.

#### Variables

| Variable                                      | Description                                           |
| --------------------------------------------- | ----------------------------------------------------- |
| `azerothcore_modules_progression_enabled`     | Enable Individual Progression support.                |
| `azerothcore_modules_progression_repository`  | Progression module repository.                        |
| `azerothcore_modules_progression_version`     | Progression module version/ref.                       |
| `azerothcore_modules_progression_phase`       | Progression phase to configure.                       |
| `azerothcore_modules_default_dictionary`      | Default dictionary of modules (IP).                   |
| `azerothcore_modules_extra_dictionary`        | Extra dictionary of modules (add new modules to this).|
| `azerothcore_modules_dictionary`              | Use this to override the default modules.             |

### `azerothcore_build`

Builds custom AzerothCore Docker images and optionally pushes them to a Docker
registry.

#### Variables

| Variable                              | Description                                                                |
| ------------------------------------- | -------------------------------------------------------------------------- |
| `azerothcore_build_images`            | Whether images should be built.                                            |
| `azerothcore_build_repository`        | AzerothCore source repository.                                             |
| `azerothcore_build_version`           | AzerothCore source version/ref.                                            |
| `azerothcore_build_repository_path`   | Path where the source repository will be cloned.                           |
| `azerothcore_build_push_images`       | Push images after building.                                                |
| `azerothcore_build_image_tag`         | Image tag applied to built images.                                         |
| `azerothcore_build_registry_address`  | Docker registry address.                                                   |
| `azerothcore_build_registry_port`     | Docker registry port.                                                      |
| `azerothcore_build_compose_overrides` | Overrides applied to the generated builder Compose configuration.          |
| `azerothcore_build_images_list`       | List of images to build (Default is worldserver, authserver and db-import) |

## Dependencies

This collection depends on:

* `ansible.posix`
* `community.docker`

## Included Playbooks

### `deploy.yml`

Runs the complete deployment workflow:

1. Prepare the `acore-docker` project.
2. Configure AzerothCore modules.
3. Optionally build custom images.
4. Deploy the Docker Compose stack.

The Docker Compose deployment state can be controlled using
`azerothcore_deploy_state`, which defaults to `present`.

```bash
ansible-playbook holliefae.azerothcore.deploy
```

### `build.yml`

Builds custom AzerothCore images without deploying the Docker Compose stack.

```bash
ansible-playbook holliefae.azerothcore.build
```

## Example Configuration

Example config for a basic deployment.

```yaml
azerothcore_install_db_pwd: "<password>"
azerothcore_install_assets_path: "<path_to_asset_data>"

```

## License

GPL-3.0-only

## Notes

AI (specifically ChatGPT) was used to help make this README as I struggle with writing documentation.
