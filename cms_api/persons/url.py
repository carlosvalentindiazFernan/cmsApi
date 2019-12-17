from .view import (
    PersonsView,
    PersonsDetailView,
    PersonsDealsView
)
"""
Router config  add Activities Resources
"""

def persons_url(path,api):
    # Router config
    api.add_resource(PersonsView, f'{path}')
    api.add_resource(PersonsDetailView, f'{path}/<person_id>')
