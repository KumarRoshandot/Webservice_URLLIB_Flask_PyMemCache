'''
This will return Tree based dependencies structure for a given package name and version
'''
import urllib.request, urllib.error
import json
import sys


class node(object):
    def __init__(self,value,children = []):
        self.value = value
        self.children = children

    def __repr__(self, level = 0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


def fetch_url_data(pack_name,version):
    URL = 'https://registry.npmjs.org/{}/{}'.format(pack_name,version)
    print(URL)

    try:
        response = urllib.request.urlopen(URL)
        js = json.loads(response.read())
    except:
        js = None
    if not js:
        return False,'==== Failure To Retrieve, check package name and version ===='
    return True,js["dependencies"]


def tree_package_dependencies(pack_name,dependencies):
    pkg_depend = node(pack_name)
    pkg_depend.children = [node("dependencies")]
    pkg_depend.children[0].children = [node(i) for i in dependencies]
    return pkg_depend


# Main calling method from another program of this file with 2 parameters
# It returns a class type value
def main(package_name,version_val):
    status, dep_data = fetch_url_data(package_name, version_val)
    if status is False:
        return status, dep_data
    else:
        tree_data = tree_package_dependencies(package_name, dep_data)
        # print(tree_data)
        return status, tree_data



