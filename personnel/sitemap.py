'''This package controls the sitemap for the personnel app. 

This sitemap will be generated at /sitemap-papers.xml
'''

from django.contrib.sitemaps import Sitemap

from personnel.models import Personnel

class LabPersonnelSitemap(Sitemap):
    '''This sitemap lists all personnel to be indexed.
    
    It only includes current laboratory members (current_lab_member=True)'''

    changefreq = 'yearly'
    priority = '0.5'
    
    def items(self):
        '''Filters Personnel to show only laboratory papers.'''
        return Personnel.objects.filter(current_lab_member=True)
        
    def lastmod(self, person):
        '''lastmod uses the last modification of the paper (not the comments).'''
        return person.date_last_modified