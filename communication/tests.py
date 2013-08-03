"""
This file contains the unit tests for the :mod:`communication` app.

Since this app has no models there is model and view tests:

* :class:`~communication.tests.CommunicationModelTests`
* :class:`~communication.tests.CommunicationViewTests` 

"""

from lab_website.tests import BasicTests

from communication.models import LabAddress,LabLocation

from personnel.models import Address

class CommunicationModelTests(BasicTests):
    '''This class tests the views associated with models in the :mod:`communication` app.'''
    
    fixtures = ['test_address',]
    
    def test_create_new_lab_address(self):
        '''This test creates a :class:`~communication.models.LabAddress` with the required information.'''
 
        test_address = LabAddress(type='Primary', address=Address.objects.get(pk=1)) #repeat for all required fields
        test_address.save()
        self.assertEqual(test_address.pk, 1) #presumes no models loaded in fixture data     
        
    def test_lab_address_unicode(self):
        '''This tests the unicode representation of a :class:`~communication.models.LabAddress`.'''
 
        test_address = LabAddress(type='Primary', address=Address.objects.get(pk=1)) #repeat for all required fields
        test_address.save()
        self.assertEqual(test_address.pk, 1) #presumes no models loaded in fixture data  
        self.assertEqual(test_address.__unicode__(), Address.objects.get(pk=1).__unicode__())
        
    def test_create_new_lab_location(self):
        '''This test creates a :class:`~communication.models.LabLocation` with the required information only.'''
 
        test_location = LabLocation(name = 'Memphis', 
            type='City', 
            priority=1) #repeat for all required fields
        test_location.save()
        self.assertEqual(test_location.pk, 1) #presumes no models loaded in fixture data         

    def test_create_new_lab_location_all(self):
        '''This test creates a :class:`~communication.models.LabLocation` with all fields included.'''
 
        test_location = LabLocation(name = 'Memphis', 
            type='City', 
            priority=1,
            address=Address.objects.get(pk=1),
            url = 'www.cityofmemphis.org',
            description = 'some description about the place',
            lattitude = 35.149534,
            longitude = -90.04898,) #repeat for all required fields
        test_location.save()
        self.assertEqual(test_location.pk, 1) #presumes no models loaded in fixture data
        
    def test_lab_location_unicode(self):
        '''This test creates a :class:`~communication.models.LabLocation` with the required information only.'''
 
        test_location = LabLocation(name = 'Memphis', 
            type='City', 
            priority=1) #repeat for all required fields
        test_location.save()
        self.assertEqual(test_location.pk, 1)
        self.assertEqual(test_location.__unicode__(), 'Memphis') 

class CommunicationViewTests(BasicTests):
    '''This class tests the views associated with the :mod:`communication` app.'''
    
    
    def test_feed_details_view(self):
        """This tests the feed-details view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/feeds')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'feed_details.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('google_calendar_id' in test_response.context)          
        
    def test_lab_rules_view(self):
        '''This tests the lab-rules view.
        
        The tests ensure that the correct template is used.
        It also tests whether the correct context is passed (if included).
        his view uses a user with superuser permissions so does not test the permission levels for this view.'''
        
        test_response = self.client.get('/lab-rules')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'lab_rules.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('lab_rules' in test_response.context)    
        self.assertTrue('lab_rules_source' in test_response.context)    
        
    def test_twitter_view(self):
        '''This tests the twitter view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/twitter')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'twitter_timeline.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('timeline' in test_response.context)         
        
    def test_calendar_view(self):
        '''This tests the google-calendar view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/calendar')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'calendar.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('google_calendar_id' in test_response.context)                    
                                
        
    def test_wikipedia_view(self):
        '''This tests the google-calendar view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/wikipedia')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'wikipedia_edits.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('pages' in test_response.context)                                 
                                
    def test_news_view(self):
        '''This tests the lab-news view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/news')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'lab_news.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('statuses' in test_response.context) 
        self.assertTrue('links' in test_response.context)           
        self.assertTrue('milestones' in test_response.context) 
        
    def test_contact_page(self):
        '''This tests the contact-page view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/contact/')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'contact.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        
    def test_location_page(self):
        '''This tests the location view.
        
        Currently it ensures that the template is loading, and that that the location_list context is passed.
        ''' 
        test_response = self.client.get('/location')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'location.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('lablocation_list' in test_response.context)                                          
