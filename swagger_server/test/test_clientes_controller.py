# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cliente import Cliente  # noqa: E501
from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClientesController(BaseTestCase):
    """ClientesController integration test stubs"""

    def test_upm_aos_clientes_cget(self):
        """Test case for upm_aos_clientes_cget

        Obtiene una lista de todos los clientes del taller
        """
        response = self.client.open(
            '/clientes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_clientes_coptions(self):
        """Test case for upm_aos_clientes_coptions

        Proporciona la lista de los métodos HTTP soportados.
        """
        response = self.client.open(
            '/clientes',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_clientes_get(self):
        """Test case for upm_aos_clientes_get

        Recupera un cliente concreto identificado por su ID.
        """
        response = self.client.open(
            '/clientes/{idCliente}'.format(id_cliente=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_clientes_get_by_nifnie(self):
        """Test case for upm_aos_clientes_get_by_nifnie

        Recupera un cliente concreto identificado por su NIF o NIE.
        """
        response = self.client.open(
            '/clientes/nifnie/{nifnie}'.format(nifnie='nifnie_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_clientes_get_by_nombre(self):
        """Test case for upm_aos_clientes_get_by_nombre

        Obtiene una lista de aquellos clientes cuyo nombre coincida con el nombre solicitado.
        """
        response = self.client.open(
            '/clientes/nombre/{nombre}'.format(nombre='nombre_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_clientes_id(self):
        """Test case for upm_aos_clientes_id

        Provides the list of HTTP supported methods.
        """
        response = self.client.open(
            '/clientes/{idCliente}'.format(id_cliente=56),
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_clientes_post(self):
        """Test case for upm_aos_clientes_post

        Registrar un cliente
        """
        body = None
        response = self.client.open(
            '/clientes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_clientes_put(self):
        """Test case for upm_aos_clientes_put

        Modifica los dados de un cliente cocreto.
        """
        body = None
        headers = [('if_match', 'if_match_example')]
        response = self.client.open(
            '/clientes/{idCliente}'.format(id_cliente=56),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
