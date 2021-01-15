import connexion
import six
from pymongo import MongoClient
from TimeSeriesIoT import util


def last_sensor_id_get(sensor_id):  # noqa: E501
    """Renvoye la dernière valeur d&#39;un capteur

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str

    :rtype: List[int]
    """
    pipeline = [{"$match": {"SENSOR": "Temp1"}}, {"$sort": {"DATE": -1}}, {"$limit": 1}]
    x = list(collection.aggregate(pipeline))
    return 'Sensor : ' + sensor_id + ' [start:end] : [' + str(start_date) + ':' + str(end_date) + '] Last ' + x[0][
        'VALUE']


def mean_sensor_id_get(sensor_id, start_date=None, end_date=None):  # noqa: E501
    """Calculer la moyenne d&#39;un capteur entre deux dates

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str
    :param start_date: Integer/timestamp of the start date
    :type start_date: int
    :param end_date: Integer/timestamp of the end date
    :type end_date: int

    :rtype: List[int]
    """
    client = MongoClient('mongodb://192.168.99.100:27017/')
    db = client.FilRouge
    collection = db.data
    pipeline = [{"$match": {"DATE": {"$gte": start_date, "$lte": end_date}, "SENSOR": "Temp1"}},
                {"$group": {"_id": {"SENSOR": "$SENSOR"}, "average": {"$avg": "$VALUE"}}}]
    x = list(collection.aggregate(pipeline))

    return 'Sensor : ' + sensor_id + ' [start:end] : [' + str(start_date) + ':' + str(end_date) + '] Average ' + x[0][
        'average']


def min_sensor_id_get(sensor_id, start_date=None, end_date=None):  # noqa: E501
    """Calculer la valeur minimum d&#39;un capteur entre deux dates

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str
    :param start_date: Integer/timestamp of the start date
    :type start_date: int
    :param end_date: Integer/timestamp of the end date
    :type end_date: int

    :rtype: List[int]
    """
    client = MongoClient('mongodb://192.168.99.100:27017/')
    db = client.FilRouge
    collection = db.data
    pipeline = [{"$match": {"DATE": {"$gte": start_date, "$lte": end_date}, "SENSOR": "Temp1"}},
                {"$group": {"_id": {"SENSOR": "$SENSOR"}, "minimum": {"$min": "$VALUE"}}}]
    x = list(collection.aggregate(pipeline))

    return 'Sensor : ' + sensor_id + ' [start:end] : [' + str(start_date) + ':' + str(end_date) + '] Minimum ' + x[0][
        'minimum']
