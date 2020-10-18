from django.db import models

# Create your models here.


from datetime import timedelta, datetime, date

from django.utils import timezone

from django.db.models import Q



class Name(models.Model):


	inTZObject_name = models.CharField(max_length=70, default='EDT')


	def __str__(self):

		return self.inTZObject_name


class NameModel(models.Model):


	inTZObject_name_var = models.CharField(max_length=70, default='EDT')


	def __str__(self):

		return self.inTZObject_name_var





class DayQuerySet(models.query.QuerySet):

	def search(self, query):
		lookup = (
				 Q(date_time_field__icontains=query) )


		return self.filter(lookup)
				






class DayModelManager(models.Manager):


	def get_queryset(self):
		    return DayQuerySet(self.model, using=self._db)



	def search(self, query=None):
			if query is None:
				return self.get_queryset.none()
			return self.get_queryset().search(query)




class Day(models.Model):

	date_time_field = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)

	first_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

	one_date_res = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	two_date_res = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)


	days_till_a_date_result = models.IntegerField(default=0)



	date_for_years_with_attributes_equal_to_a_value = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	date_for_years_with_attributes_equal_to_a_value_result = models.IntegerField(default=0)
	value_for_attributes = models.IntegerField(default=0)
	attributes_sum = models.IntegerField(default=0)


	first_year_of_decade = models.IntegerField(default=0)
	second_year_of_decade = models.IntegerField(default=0)
	bisect_years = models.TextField(default=0)
	days_in_a_decade = models.IntegerField(default=0)
	bisect_years_count = models.IntegerField(default=0)


	first_year_of_century = models.IntegerField(default=0)
	second_year_of_century = models.IntegerField(default=0)
	bisect_years_in_century = models.TextField(default=0)
	days_in_a_century = models.IntegerField(default=0)
	bisect_years_count_in_century = models.IntegerField(default=0)


	date_to_sum_attributes = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	date_to_sum_attributes_result = models.IntegerField(default=0)
	date_to_sum_attributes_days = models.IntegerField(default=0)
	nth_day_value = models.IntegerField(default=0)
	nth_month_value = models.IntegerField(default=0)


	first_date_bisect_years_in_centuries = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date_bisect_years_in_centuries = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	bisect_years_in_centuries = models.TextField(default=0)
	days_in_centuries = models.IntegerField(default=0)
	bisect_years_count_in_centuries = models.IntegerField(default=0)


	first_date_next_spring_equinox = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date_next_spring_equinox = models.DateField(auto_now=False, auto_now_add=False, default=date(2021,3,20))
	months_until_next_spring_equinox = models.IntegerField(default=0)
	days_until_next_spring_equinox = models.IntegerField(default=0)



	first_date_next_autumn_equinox = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date_next_autumn_equinox = models.DateField(auto_now=False, auto_now_add=False, default=date(2021,9,22))
	months_until_next_autumn_equinox = models.IntegerField(default=0)
	days_until_next_autumn_equinox = models.IntegerField(default=0)


	first_date_with_total_lunar_eclipse = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date_with_total_lunar_eclipse = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	months_between_dates_with_total_lunar_eclipse = models.IntegerField(default=0)
	minutes_between_dates_with_total_lunar_eclipse = models.IntegerField(default=0)

	inTimeDelta_hours = models.IntegerField(default=0)
	inTZObject_name = models.CharField(max_length=70, default='EDT')
	datetime_instance_var = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	first_date_time_var = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	second_date_time_var = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)


	inTimeDelta_hours_diff = models.IntegerField(default=0)
	inTZObject_name_diff = models.CharField(max_length=70, default='EDT')
	datetime_instance_var_diff = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	first_date_time_var_diff = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	second_date_time_var_diff = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)

	timezone_diff_days= models.IntegerField(default=0)
	timezone_diff_minutes = models.IntegerField(default=0)


	inTZObject_name_field = models.ManyToManyField(Name)
	inTZObject_name_diff_filed = models.ManyToManyField(NameModel)

	your_address =  models.CharField(max_length=150, default='name and street number city')

	address_to_search =  models.CharField(max_length=150, default='name and street number city')

	inTimeDelta_hours_to_search = models.IntegerField(default=0)

	inTimeDelta_hours_res = models.IntegerField(default=0)

	# diff_in_hours_with_local_time = models.IntegerField(default=0)


	used_in_calculations_by_user = models.BooleanField(default=False)



	pivot_value = models.IntegerField(default=1)

	n_days = models.IntegerField(default=0)

	year_for_date_n_days = models.IntegerField(default=0)

	month_for_date_n_days = models.IntegerField(default=0)

	date_for_the_next_n_days = models.TextField(default=0)


	

	first_year_in_a_decade_sum_attributes = models.IntegerField(default=0)

	second_year_in_a_decade_sum_attributes = models.IntegerField(default=0)

	month_sum_attributes = models.IntegerField(default=0)

	day_sum_attributes = models.IntegerField(default=0)

	hour_sum_attributes = models.IntegerField(default=0)

	minute_sum_attributes = models.IntegerField(default=0)

	second_sum_attributes = models.IntegerField(default=0)
	

	dates_sum_attributes_result = models.TextField(default=0)




	first_year_in_a_century_sum_attributes = models.IntegerField(default=0)

	second_year_in_a_century_sum_attributes = models.IntegerField(default=0)

	month_sum_attributes_in_a_century = models.IntegerField(default=0)

	day_sum_attributes_in_a_century = models.IntegerField(default=0)
	
	hour_sum_attributes_in_a_century = models.IntegerField(default=0)

	minute_sum_attributes_in_a_century = models.IntegerField(default=0)

	second_sum_attributes_in_a_century = models.IntegerField(default=0)


	dates_sum_attributes_in_a_century_result = models.TextField(default=0)




	nth_day_time_until = models.IntegerField(default=0)

	n_years_time_until = models.IntegerField(default=0)

	first_date_time_until = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	second_date_time_until = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)

	days_until_result = models.IntegerField(default=0)

	time_until_result = models.TextField(default=0)

	

	next_solstice = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime(2021, 12, 21, 10, 0, 0))

	days_until_solstice = models.IntegerField(default=0)

	date_and_time_until_solstice = models.TextField(default=0)




	year_one_next_n_years = models.IntegerField(default=0)

	year_two_next_n_years = models.IntegerField(default=0)

	day_next_n_years = models.IntegerField(default=0)

	month_next_n_years = models.IntegerField(default=0)

	date_and_time_until_nth_day_in_the_next_n_years = models.TextField(default=0)


	

	first_year_of_nth_century_attributes = models.IntegerField(default=0)

	second_year_of_nth_century_attributes = models.IntegerField(default=0)

	n_days_attributes = models.IntegerField(default=0)

	datetime_attributes = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)


	n_days_attributes_result = models.TextField(default=0)





	first_year_solstice_even_sum = models.IntegerField(default=0)
	second_year_solstice_even_sum = models.IntegerField(default=0)

	ssolsticel_even_sum = models.TextField(default=0)

	wsolsticel_even_sum = models.TextField(default=0)

	solsticel_even_sum = models.TextField(default=0)

	ssolsticel_even_sum_count = models.IntegerField(default=0)

	wsolsticel_even_sum_count = models.IntegerField(default=0)

	solsticel_even_sum_count = models.IntegerField(default=0)




	first_year_solstice_odd_sum = models.IntegerField(default=0)
	second_year_solstice_odd_sum = models.IntegerField(default=0)

	ssolsticel_odd_sum = models.TextField(default=0)

	wsolsticel_odd_sum = models.TextField(default=0)

	solsticel_odd_sum = models.TextField(default=0)

	ssolsticel_odd_sum_count = models.IntegerField(default=0)

	wsolsticel_odd_sum_count = models.IntegerField(default=0)

	solsticel_odd_sum_count = models.IntegerField(default=0)




	objects = DayModelManager() 



	# def __str__(self):

	# 	return str(self.date_time_field)





class DaysInSearchEngine(models.Model):

		date_field = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

		spring_equinox = models.BooleanField(default=False)

		autumn_equinox = models.BooleanField(default=False)

		summer_solstice = models.BooleanField(default=False)

		winter_solstice = models.BooleanField(default=False)

		total_lunar_eclipse = models.BooleanField(default=False)

		season=models.CharField(max_length=25, default="name")

		stars = models.TextField(default="names")

		stars_movement = models.TextField(default="eliptical")















