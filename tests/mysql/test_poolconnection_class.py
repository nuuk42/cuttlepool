# -*- coding: utf-8
"""
Tests related to the PoolConnection class.
"""
from cuttlepool.cuttlepool import PoolConnection

from test_cuttlepool_class import CuttlePoolTestCase


class PoolConnectionGetAttrTestCase(CuttlePoolTestCase):

    def test_poolconnection_getattr(self):
        con = PoolConnection(self.cp._make_connection(), self.cp)
        self.assertEqual(con.cursor, con._connection.cursor)

    def test_poolconnection_getattr_close(self):
        con = PoolConnection(self.cp._make_connection(), self.cp)
        self.assertNotEqual(con.close, con._connection.close)


class PoolConnectionCloseTestCase(CuttlePoolTestCase):

    def test_poolconnection_close(self):
        con = PoolConnection(self.cp._make_connection(), self.cp)

        # return the connection to the pool
        self.assertEqual(self.cp._pool.qsize(), 0)
        con.close()
        self.assertEqual(self.cp._pool.qsize(), 1)

        # check that connection and pool are no longer in con object
        self.assertIsNone(con._connection)
        self.assertIsNone(con._pool)