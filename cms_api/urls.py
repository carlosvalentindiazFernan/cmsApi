from .activities.urls import activities_url
from .deal.urls import deal_url
from cms_api.utils.http import Http

"""
    Global config urls path
"""

def urls_path(app,api):
    # Activies Modul
    activities_url('/api/v1/activities',api)
    # Deal Modul
    deal_url('/api/v1/deal',api)


    # Error 404
    @app.errorhandler(404)
    def page_not_found(error):  
        return {'404.html':'404'}


