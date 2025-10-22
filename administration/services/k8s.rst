Kubernetes
##########

Overview
--------

The `Kubernetes <https://kubernetes.io/>`_ service in |omv| is designed to manage and orchestrate
containerized applications using the Kubernetes platform. It provides a
user-friendly interface to deploy and manage applications in a cluster
environment.

The Kubernetes service can be installed via the `openmediavault-k8s` plugin.

The lightweight `K3s <https://k3s.io/>`_ is used under the hood, allowing a
Kubernetes environment to run on SBC systems as well.

The installed applications can then be accessed via the URL:

.. code-block:: none

    https://<app>.<hostname>.<domainname>

.. note::
    It is important that the local router can resolve `<hostname>.<domainname>`.

Using subdomains (e.g., `app.mynas.internal`) is preferred over path prefixes
(e.g., `mynas.internal/app`) for accessing apps via the Traefik reverse proxy
in the |omv| Kubernetes plugin because:

- Cleaner and simpler routing – Subdomains keep Ingress rules modular and avoid complex path rewrites.
- Fewer compatibility issues – Many apps assume they run at / and break when served under a path prefix due to issues with relative URLs, static assets, or routing.
- Avoids URL rewriting problems – With path prefixes, you often need to rewrite URLs or modify the app, which can cause subtle bugs or failures.
- Better isolation and security – Subdomains help enforce security boundaries between apps.
- Easier scaling and maintenance – Apps on subdomains are more portable, scalable, and microservice-friendly.

Recipes
-------

The Kubernetes service offers several, so called, recipes to help you get
started with installing popular applications.

The recipes are maintained in the `openmediavault-k8s-recipes GitHub project <https://github.com/openmediavault/openmediavault-k8s-recipes>`_
and are offered by the plugin in a graphical overview for easy installation.

The recipes have an area at the top of the YAML code that must be filled in
by the user. This configuration area contains information that is then used
by the recipe to install the application on the given system.

Installed applications are not updated by |omv|, this must be done by the
user. In most cases, it is sufficient to first delete the image and then
the pod of the application to be updated.

Administration
--------------

|omv| offers a rudimentary UI for managing simple tasks in the cluster, but
it makes sense to use external software that specializes in this area.
Examples include `Rancher UI <https://www.rancher.com/>`_ (to be installed using a recipe) or `k9s <https://k9scli.io/>`_.

Customization
-------------

The Kubernetes service in |omv| is can be customized via :ref:`environment variables <environmental_variable>` to adapt it to your personal needs.

.. list-table::
  :widths: 20 30 45
  :header-rows: 1

  * - Environment variable
    - Example
    - Description
  * - OMV_K8S_K3S_VERSION
    - ``v1.33.5+k3s1``
    - Specifies the K3s version to be used.
  * - OMV_K8S_TRAEFIK_PORTS
    - ``{foo: {exposedPort: 3456}}``
    - Defines additional ports (`entry points <https://doc.traefik.io/traefik/reference/install-configuration/entrypoints/>`_)
      to be used by the Traefik reverse proxy.
