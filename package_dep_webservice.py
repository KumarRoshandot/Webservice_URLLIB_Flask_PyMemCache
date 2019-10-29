from synk_task import package_dependencies
from flask import Flask, jsonify
from pymemcache.client import base


def create_app():
    app = Flask(__name__)
    # Setting a cache timeout of 2 hour
    # Make sure to run memcached before running below command
    cache = base.Client('localhost', 11211, timeout=7200)

    @app.route('/dependencies/<package>/<version>')
    def get_dependencies(package, version):
        '''
        Find all Dependencies of a package for a mentioned version

        Args:
            package: A package name, e.g. 'express'
            version: Version value , e.g. 2.1.0 or latest

        Returns:
            JSON encoded tree formatted dependencies
        '''

        # First it will check cache if not present then go fetch from URL
        if cache.get('{}{}'.format(package, version)) is not None:
            return cache.get('{}{}'.format(package, version))

        # This is only when the results are not present in cache
        status, dependencies = package_dependencies.main(package, version)
        # print(dependencies)

        if status is False:
            jsonified = jsonify({"ERROR 404 :":dependencies})
            return jsonified

        # make data serializable
        jsonified = jsonify({"dependencies":dependencies})
        cache.set('{}{}'.format(package, version), jsonified)
        return jsonified

    app.run(debug=True)


if __name__ == "__main__":
    # Create an app 'http://127.0.0.1:5000/dependencies/<package>/<version>'
    create_app()

    # For testing
    # status, result = package_dependencies.main('express', 'lat1est')
    # print(result)

