export PYRO_SERIALIZER='pickle'
export PYRO_SERIALIZERS_ACCEPTED='pickle'
export PYRO_SOCK_REUSE=True
export PYRO_PICKLE_PROTOCOL_VERSION=2

python -m Pyro4.naming -n 0.0.0.0
