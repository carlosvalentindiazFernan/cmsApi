from .view import DealView,DealsDetailVIew
"""
Router config  add Deal Resources, url
"""

def deal_url(path,api):
    # Router config
    api.add_resource(DealView, f'{path}')
    api.add_resource(DealsDetailVIew, f'{path}/<deal_id>')