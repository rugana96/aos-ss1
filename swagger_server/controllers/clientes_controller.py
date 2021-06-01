import connexion
import six

from swagger_server.models.cliente import Cliente  # noqa: E501
from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def upm_aos_clientes_cget():  # noqa: E501
    """Obtiene una lista de todos los clientes del taller

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def upm_aos_clientes_coptions():  # noqa: E501
    """Proporciona la lista de los métodos HTTP soportados.

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def upm_aos_clientes_get(id_cliente):  # noqa: E501
    """Recupera un cliente concreto identificado por su ID.

    Devuelve el cliente identificado por &#x60;idCliente&#x60;. # noqa: E501

    :param id_cliente: ID del cliente
    :type id_cliente: int

    :rtype: Cliente
    """
    return 'do some magic!'


def upm_aos_clientes_get_by_nifnie(nifnie):  # noqa: E501
    """Recupera un cliente concreto identificado por su NIF o NIE.

    Devuelve el cliente identificado por &#x60;nif/nie&#x60;. # noqa: E501

    :param nifnie: El NIE o NIF del cliente
    :type nifnie: str

    :rtype: Cliente
    """
    return 'do some magic!'


def upm_aos_clientes_get_by_nombre(nombre):  # noqa: E501
    """Obtiene una lista de aquellos clientes cuyo nombre coincida con el nombre solicitado.

    Devuelve el cliente identificado por &#x60;nombre&#x60;. # noqa: E501

    :param nombre: El nombre del cliente
    :type nombre: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def upm_aos_clientes_id(id_cliente):  # noqa: E501
    """Provides the list of HTTP supported methods.

    Devuelve una cabecera &#x60;Allow&#x60; con la lista de métodos HTTP soportados. # noqa: E501

    :param id_cliente: ID del cliente
    :type id_cliente: int

    :rtype: None
    """
    return 'do some magic!'


def upm_aos_clientes_post(body):  # noqa: E501
    """Registrar un cliente

    Registra un nuevo cliente y lo almacena en la base de datos # noqa: E501

    :param body: &#x60;Cliente&#x60; data
    :type body: dict | bytes

    :rtype: Cliente
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def upm_aos_clientes_put(body, if_match, id_cliente):  # noqa: E501
    """Modifica los dados de un cliente cocreto.

    Actualiza los datos de un cliente identificado por &#x60;idCliente&#x60;. # noqa: E501

    :param body: &#x60;Cliente&#x60; data
    :type body: dict | bytes
    :param if_match: ETag del recurso que se desea modificar
    :type if_match: str
    :param id_cliente: ID del cliente
    :type id_cliente: int

    :rtype: Cliente
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
