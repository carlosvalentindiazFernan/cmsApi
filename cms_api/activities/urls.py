from .view import ActivitiesView
"""
Router config  add Activities Resources
"""

def activities_url(path,api):
    # Router config
    api.add_resource(ActivitiesView, f'{path}')
