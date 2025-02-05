from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class UserManager(BaseUserManager):
  def create_user(self, first_name, last_name, username, email, password=None):
    if not email:
      raise ValueError('User must have an email address')
    
    if not username:
      raise ValueError('User must have a username')
    
    user = self.model(
      email=self.normalize_email(email),
      username=username,
      first_name=first_name,
      last_name=last_name
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, first_name, last_name, username, email, password=None):
    user = self.create_user(
      email=self.normalize_email(email),
      username=username,
      first_name=first_name,
      last_name=last_name,
      password=password
    )
    user.is_admin = True
    user.is_active = True
    user.is_staff = True
    user.is_superadmin = True
    user.is_superuser = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser, PermissionsMixin):
  
  ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('attendee', 'Attendee')  
  )
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  role = models.CharField(choices=ROLE_CHOICES, default='attendee')
  address = models.TextField(null=True, blank=True)
  phone_number = models.CharField(max_length=15, null=True, blank=True)
  profile_picture = CloudinaryField('image', default='placeholder')  
  country = models.CharField(max_length=15, blank=True, null=True)

  # Required fields
  date_joined = models.DateTimeField(auto_now_add=True)   
  last_login = models.DateTimeField(auto_now_add=True)  
  created_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True) 
  is_admin = models.BooleanField(default=False) 
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superadmin = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  objects = UserManager()

  def __str__(self):
    return self.email
  
  def has_perm(self, perm, obj=None):
    return self.is_admin
  
  def has_module_perms(self, app_label):
    return True

