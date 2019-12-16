from .view import ActivitiesView,ActivityView
"""
Router config  add Activities Resources
"""

def activities_url(path,api):
    # Router config
    api.add_resource(ActivitiesView, f'{path}')
    api.add_resource(ActivityView, f'{path}/<activity_id>')


