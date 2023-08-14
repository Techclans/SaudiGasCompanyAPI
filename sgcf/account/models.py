from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,Group,PermissionsMixin,Permission
#from UserType.models import UserType


#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, tc, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          tc=tc,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, tc, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          tc=tc,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser,PermissionsMixin):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200)
  tc = models.BooleanField()
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  #UserTypeId = models.ForeignKey('UserType.UserType',on_delete=models.CASCADE,related_name='UserTypeId', blank=True, null=True,db_column='UserTypeId')  # Field name made lowercase.
  is_superuser =  models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  mobile_number = models.CharField(max_length=20, blank=True)
  groups = models.ManyToManyField(Group, related_name='user', blank=True)
 # OrgId = models.ForeignKey('Organisation.Organization',on_delete=models.CASCADE,related_name='OrgId', blank=True, null=True,db_column='OrgId')  # Field name made lowercase.
  user_permissions = models.ManyToManyField(
        Permission,
        related_name='user',
        blank=True,
    )

  objects = UserManager()



  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'tc']



  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      #return perm
      return perm in self.get_all_permissions()

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin

class CustomGroup(Group):
    # Add any additional fields to your group model
    pass

class CustomPermission(Permission):
    # Add any additional fields to your custom permission model
    pass
