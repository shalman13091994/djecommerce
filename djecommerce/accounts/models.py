from django.db import models
from django.contrib.auth.models import(AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.countries.fields import CountryField
from django.utils.translation import gettext_lazy as _ 

class CustomAccountManger(BaseUserManager):
    # custom account manager to manage the user and superuser

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('sUPER USER MUST BE ASSIGNED TO is_staff =True'))

        if other_fields.get('is_active') is not True:
            raise ValueError(_('sUPER USER MUST BE ASSIGNED TO is_active =True'))

        return self.create_user(email, user_name, password, **other_fields)
# we need these fields to populate for superuser now user_name will be replaced by email 
# USERNAME_FIELD = 'email' REQUIRED_FIELDS = ['user_name'] 


    def create_user(self, email, user_name, password, **otherfields):

        if not email:
            raise ValueError(_('Youst must provide email address'))

        email = self.normalize_email(email)
        # after validating the fields where things r entering the properly
        user = self.model(email = email, user_name= user_name, **otherfields)

        user.set_password(password)
        user.save()
        return user



class UserBase(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique = True)
    user_name = models.CharField(max_length=150, unique = True)
    first_name = models.CharField(max_length=150,blank=True)
    about = models.TextField(_('about', max_length = 500, blank =True))

    # Delivery details
    country = CountryField()
    phone_number = models.PhoneNumberField(max_length=10, blank=True)
    address_line_1= models.CharField(max_length=150, blank=True)
    address_line_2 = models.CharField(max_length=150, blank=True)
    post_code = models.CharField(max_length=7, blank=True)
    town_city = models.CharField(max_length=150, blank=True)
    
    #USER STATUS - we dont user to get delete we can disable the user to save the user's data
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    # custom account manager to manage the user and superuser
    objects = CustomAccountManger()
    # for custom account manager 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name'] #username mandatory

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'
    
    def __str__(self) :
        return self.user_name




