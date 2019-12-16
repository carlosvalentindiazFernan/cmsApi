from .view import DealView
"""
Router config  add Deal Resources, url
"""

def deal_url(path,api):
    # Router config
    api.add_resource(DealView, path)
