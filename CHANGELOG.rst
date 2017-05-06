#####################
Cuttle Pool Changelog
#####################

Here are the changes made to Cuttle Pool for each release.

Version 0.3.0
-------------

Minor release, unreleased

- Changed ``_collect_lost_connections()`` to ``_harvest_lost_connections()``.
- ``get_connection()`` now calls ``_harvest_lost_connections()`` before
  attempting to get a connection from the pool if the pool is empty.
- ``CuttlePool`` object now requires a ``connect`` argument, which is a
  ``connect()`` method of the chosen sql driver.
- ``CuttlePool`` is now meant to be subclassed with user specified functions
  ``normalize_connection()`` and ``ping()``.
- ``get_connection()`` will now ping the connection according to a user defined
  function ``ping()``.
- ``get_connection()`` will reset the connection properties according to a
  user defined function ``normalize_connection()``.
- The pool can be emptied with ``empty_pool``.

Version 0.2.1
-------------

- Fix classifier in ``setup.py`` which caused error during upload.

Version 0.2.0
-------------

- PoolConnection and cursors module are importable from cuttlepool instead of
  cuttlepool.cuttlepool.
- ``get_connection()`` will only search for lost connections if it can't get an
  initial connection from the pool or make a connection.
- The connection object in ``get_connection()`` is pinged right before
  returning a ``PoolConnection`` and if the ping fails, the connection is
  replaced.
- ``connection_arguments`` property added which returns a copy of the connection
  arguments.

Version 0.1.0
-------------

Initial release.
