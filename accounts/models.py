from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group, Permission
from django.db import models
from django.urls import reverse


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        
    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})
    


class MyUser(AbstractBaseUser):
    # This is a custom user model
    STATUS_CHOICES = [
        ('full-time', 'Full-time'),
        ('intern', 'Intern'),
        ('attachee', 'Attachee'),
    ]

    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,null=True)
    email = models.EmailField(unique=True)
    dob = models.DateField(verbose_name="date of birth",null=True)
    phone = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    arrangement = models.CharField(max_length=50, choices=STATUS_CHOICES,default='full-time')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dob']

    objects = MyUserManager()
    
    def has_module_perms(self, app_label):
        """
        Return True if the user has any permissions in the given app label.
        """
        return True

    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission.
        """
        return True

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def days_taken(self):
        leave_requests = self.leave_requests.filter(employee=self,status='Approved')
        total_days = sum(leave.days_taken.days for leave in leave_requests if leave.days_taken)
        return total_days
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})
    

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'