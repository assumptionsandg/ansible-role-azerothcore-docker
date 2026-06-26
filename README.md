# Ansible Role AzerothCore Docker

Deploys an [AzerothCore](https://www.azerothcore.org/) Docker environment using the official `acore-docker` project. The role automates cloning the required repositories, building custom server images, deploying the Docker Compose stack, and optionally integrating the Individual Progression module.

This project has no affiliation with AzerothCore.

## Features

* Clone the official `acore-docker` repository.
* Build a custom AzerothCore server from source.
* Build and push custom images.
* Deploy the complete Docker Compose project.
* Mount custom modules and configuration.
* Support the Individual Progression module. (image build required for C++ module support).
* Override both the builder and Docker Compose configuration without modifying upstream repositories.

## Requirements

The target host should have:

* Docker
* Docker Compose
* Docker Registry (by default is assumed running on the Ansible host on port 5000)
* Git
* Sufficient disk space for building AzerothCore images (default docker path in /var/lib/docker)

## Role Variables

### General

| Variable                             | Description                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `azerothcore_docker_project_path`    | Docker Compose project directory. (where upstrem compose will be copied to.)                                                                      |
| `azerothcore_docker_modules_path`    | Directory containing AzerothCore modules.                                                                                                         |
| `azerothcore_docker_config_path`     | Server configuration directory.                                                                                                                   |
| `azerothcore_docker_assets_path`     | Client data directory.                                                                                                                            |
| `azerothcore_docker_phpmyadmin_port` | Port where phpmyadmin (database web UI) will be exposed.                                                                                          |
| `azerothcore_docker_state`           | Desired Compose state. Set to `install` to run install/build only. See docs on `community.docker.docker_compose_v2` `state` option for more info. |


### AzerothCore Compose Repository

| Variable                                | Description                               |
| --------------------------------------- | ----------------------------------------- |
| `azerothcore_docker_compose_repository`         | `acore-docker` repository.                |
| `azerothcore_docker_compose_repository_version` | Version of the `acore-docker` repository. |
| `azerothcore_docker_compose_repository_path`    | Path where `acore-docker` will be cloned. |

### Container image build

| Variable                                     | Description                                    |
| -------------------------------------------- | ---------------------------------------------- |
| `azerothcore_docker_build_images`            | Whether to build images (default is false).    |
| `azerothcore_docker_builder_repository`      | AzerothCore source repository.                 |
| `azerothcore_docker_builder_version`         | Version of the builder repository.             |
| `azerothcore_docker_builder_repository_path` | Path where `azerothcore-wotlk` will be cloned. |

### Individual Progression (optional Vanilla/TBC realistic progression mod)

| Variable                                    | Description                     |
| ------------------------------------------- | ------------------------------- |
| `azerothcore_docker_progression_enabled`    | Enable progression support.     |
| `azerothcore_docker_progression_repository` | Progression module repository.  |
| `azerothcore_docker_progression_version`    | Module revision.                |
| `azerothcore_docker_progression_phase`      | Progression phase to configure. |

### Docker Registry configuration

| Variable                                  | Description                                                            |
| ----------------------------------------- | -----------------------------------------------------------------------|
| `azerothcore_docker_registry_port`        | Registry port.                                                         |
| `azerothcore_docker_registry_address`     | Registry address (assumes a registry is deployed on the ansible host). |
| `azerothcore_docker_push_images_on_build` | Push images after building. (if build is enabled)                      |
| `azerothcore_docker_image_tag`            | Image tag applied to builds.                                           |

### Database

| Variable                    | Description                          |
| --------------------------- | ------------------------------------ |
| `azerothcore_docker_db_pwd` | MariaDB root password. **Required.** |

### Compose Overrides

`azerothcore_docker_compose_overrides` allows callers to customise the generated Docker Compose configuration.

This can be used to:

* Mount additional modules (untested).
* Replace Docker images.
* Override health checks.
* Expose additional ports.
* Add custom volumes.

`azerothcore_docker_builder_overrides` similarly allows customisation of the generated builder configuration before images are built.

## Dependencies

This role has no required Ansible Galaxy dependencies.

## Example Playbook

```yaml
- hosts: game_servers
  become: true
  roles:
    - role: azerothcore_docker
```

## Example Configuration

```yaml
azerothcore_docker_progression_enabled: true
azerothcore_docker_progression_phase: 7 # Vanilla Phase 6

azerothcore_docker_registry_enabled: true
azerothcore_docker_build_images: true

azerothcore_docker_db_pwd: <password>
```

## License

GPL v3.0

## Notes

AI (specifically ChatGPT) was used to help make this README as I struggle with writing documentation.
