from django.shortcuts import render, redirect

# Create your views here.

import datetime

from datetime import date, timedelta

from datetime import datetime as datetime_function

from datetime import timezone as tzinfo_class

from django.utils import timezone


import math

from franges import frange

import geopy

from geopy.geocoders import Nominatim



# from datetime import timedelta, datetime, date  


# from dateutil.relativedelta import relativedelta


from.forms  import (DaysTillaDateForm, YearsWithAttributesEqualToaValueForm,

BisectYearsinaDecadeForm, BisectYearsinaCenturyForm,

AttributesofnthDayForm, BisectYearsinCenturiesForm, 

MonthsandDaystillthenextSpringEquinoxForm,

MonthsandDaystillthenextAutumnEquinoxForm, 

PeriodsbetweenDateswithTotalLunarEclipseForm,

Find_the_equivalent_of_timezone_with_USA_Form,

Find_the_difference_of_timezone_with_USA_Form,

Find_equivalent_with_timezone_Form,

Find_difference_of_timezone_from_UTC_Form,

find_difference_between_two_timezones_Form,

Find_difference_with_timezone_Form,

display_date_for_the_next_n_days_Form,

attributes_of_time_equal_to_date_in_a_decade_Form,

attributes_of_time_equal_to_date_in_a_century_Form,

find_time_until_a_date_after_n_years_Form,

calculate_date_and_time_until_next_solstice_Form,

date_and_time_until_the_nth_day_in_the_next_n_years_Form,

years_of_nth_century_have_more_than_n_days_with_attrs_Form,

solstices_in_n_years_with_sum_attrs_even_number_Form,

solstices_in_n_years_with_sum_attrs_odd_number_Form,

view_calendar_Form,

create_Days_Form,

create_Days_712_Form,

delete_Days_Form,

determine_visibility_Form,

ref_magnitudes_Form,

determine_most_visible_periods_Form,

set_season_Form,

determine_most_visible_periods_seasons_Form,

set_spring_equinox_Form,

set_autumn_equinox_Form,

set_summer_solstice_Form,

set_winter_solstice_Form,

determine_stars_movement_Form,)




from .models import Day, DaysInSearchEngine, Stars

from dateutil import parser



def view_days_till_a_date(request):

	if request.method == 'POST':

		form = DaysTillaDateForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			obj.days_till_a_date_result = (obj.second_date-obj.first_date).days

			obj.used_in_calculations_by_user = True

			obj.save()

			form = DaysTillaDateForm()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form = DaysTillaDateForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/days-till-a-date.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def view_days_till_a_date_display_attributes(request):

	if request.method == 'POST':

		form = DaysTillaDateForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			obj.days_till_a_date_result = (obj.second_date-obj.first_date).days

			obj.one_date_res = datetime.datetime(obj.first_date.year, obj.first_date.month,
				obj.first_date.day, timezone.now().hour, timezone.now().minute, timezone.now().second)


			obj.two_date_res = datetime.datetime(obj.second_date.year, obj.second_date.month,
				obj.second_date.day, timezone.now().hour, timezone.now().minute, timezone.now().second)

			obj.used_in_calculations_by_user = True

			obj.save()

			form = DaysTillaDateForm()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form = DaysTillaDateForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/days-till-a-date-display-attributes.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def view_years_with_equal_sum_of_attributes_to_a_value(request):

	
	if request.method == 'POST':

		form = YearsWithAttributesEqualToaValueForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			dt_obj = parser.parse(str(obj.date_for_years_with_attributes_equal_to_a_value))

			obj_d = date.fromordinal(dt_obj.toordinal())

			var = (sum(map(int, str(obj_d.year))) + obj_d.month + obj_d.day)

			if var == obj.value_for_attributes:
    
   				var1 = obj_d.year

   				obj.date_for_years_with_attributes_equal_to_a_value_result = var1

   				obj.used_in_calculations_by_user = True


   				obj.save()

   				form = YearsWithAttributesEqualToaValueForm()

			else:

				var2 = var

				obj.attributes_sum = var2

				obj.used_in_calculations_by_user = True

				obj.save()

				form = YearsWithAttributesEqualToaValueForm()
	else:

		form = YearsWithAttributesEqualToaValueForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/attributes-equal-to-a-value.html"

	return render(request, template_path, {'form': form, "obj":obj, })







def view_leap_years_in_a_decade(request):

	# pass

	if request.method == 'POST':

		form = BisectYearsinaDecadeForm(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			if obj.second_year_of_decade - obj.first_year_of_decade == 10:


				dl=[]

				count = 0

				dl_years = [i for i in range(obj.first_year_of_decade, obj.second_year_of_decade+1)]


				d = date(obj.first_year_of_decade, 1, 1)

				dt = date(obj.second_year_of_decade, 1, 1)


				td = dt - d

				obj.days_in_a_decade = td.days


				for i in dl_years:

					dl.append(date(i, 1, 1))


				obj.bisect_years = " "
	            	


				for i in dl:

				    if (i.year % 4) == 0:
				        if (i.year % 100) == 0:

				        	if (i.year % 400) == 0:
				        		obj.bisect_years+=(str(i.year)+ ", ")
				        		count += 1
				                # print("{0} is a leap year".format(i.year))
				              
				            # else:
				            #     print("{0} is not a leap year".format(i.year))
				        else:
				            # print("{0} is a leap year".format(i.year))
				            obj.bisect_years+=(str(i.year)+ ", ")

				            count += 1
				    # else:
				    #     print("{0} is not a leap year".format(i.year))

				obj.bisect_years_count = count

				obj.used_in_calculations_by_user = True


				obj.save()

				form = BisectYearsinaDecadeForm()
	else:

		form = BisectYearsinaDecadeForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/bisect-years-in-a-decade.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def view_leap_years_in_a_century(request):

	# pass

	if request.method == 'POST':

		form = BisectYearsinaCenturyForm(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			if obj.second_year_of_century - obj.first_year_of_century == 100:



				dl=[]

				count = 0

				dl_years = [i for i in range(obj.first_year_of_century, obj.second_year_of_century+1)]


				d = date(obj.first_year_of_century, 1, 1)

				dt = date(obj.second_year_of_century, 1, 1)


				td = dt - d

				obj.days_in_a_century = td.days


				for i in dl_years:

					dl.append(date(i, 1, 1))


				obj.bisect_years_in_century = " "
	            	


				for i in dl:

				    if (i.year % 4) == 0:
				        if (i.year % 100) == 0:

				        	if (i.year % 400) == 0:
				        		obj.bisect_years_in_century+=(str(i.year)+ ", ")
				        		count += 1
				                # print("{0} is a leap year".format(i.year))
				              
				            # else:
				            #     print("{0} is not a leap year".format(i.year))
				        else:
				            # print("{0} is a leap year".format(i.year))
				            obj.bisect_years_in_century+=(str(i.year)+ ", ")

				            count += 1
				    # else:
				    #     print("{0} is not a leap year".format(i.year))

				obj.bisect_years_count_in_century = count

				obj.used_in_calculations_by_user = True


				obj.save()

				form = BisectYearsinaCenturyForm()
	else:

		form = BisectYearsinaCenturyForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/bisect-years-in-a-century.html"

	return render(request, template_path, {'form': form, "obj":obj, })





   	



def view_sum_of_attributes_of_nth_day_in_a_year(request):


	if request.method == 'POST':

		form = AttributesofnthDayForm(request.POST)


		if form.is_valid():
	
			form.save()

			obj = Day.objects.last()



			if (obj.nth_day_value > 0 and obj.nth_month_value > 0):


				dl =[]

				dly = [obj.date_to_sum_attributes]

				dli = []

				# d = date(obj.date_to_sum_attributes.year, obj.nth_month_value, obj.nth_day_value)

				# dt = date(d*2)

				# td = dt - d 

				# obj.date_to_sum_attributes_days = dt.days

				for i in dly:

					dl.append(date(i.year, 1, 1))

				for i in dl:

					dli.append(i.replace(day=obj.nth_day_value, month=obj.nth_month_value))

				for i in dli:

					var = sum(map(int, str(i.year))) + i.month + i.day


				obj.date_to_sum_attributes_result = var

				obj.used_in_calculations_by_user = True



				obj.save()

				form = AttributesofnthDayForm()


	else:

		form = AttributesofnthDayForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/sum-of-attributes-of-nth-day.html"

	return render(request, template_path, {'form': form, "obj":obj, })





def view_how_many_bisect_years_in_the_last_nth_centuries(request):


	# pass

	if request.method == 'POST':

		form = BisectYearsinCenturiesForm(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			if (obj.second_date_bisect_years_in_centuries.year -  
			obj.first_date_bisect_years_in_centuries.year  > 100):


				dl=[]

				count = 0

				dl_years = [i for i in range(obj.first_date_bisect_years_in_centuries.year, 
					obj.second_date_bisect_years_in_centuries.year)]


				d = date(obj.first_date_bisect_years_in_centuries.year, 1, 1)

				dt = date(obj.second_date_bisect_years_in_centuries.year, 1, 1)


				td = dt - d

				obj.days_in_centuries = td.days


				for i in dl_years:

					dl.append(date(i, 1, 1))


				obj.bisect_years_in_centuries = " "
	            	


				for i in dl:

				    if (i.year % 4) == 0:
				        if (i.year % 100) == 0:

				        	if (i.year % 400) == 0:
				        		obj.bisect_years_in_centuries+=(str(i.year)+ ", ")
				        		count += 1
				                # print("{0} is a leap year".format(i.year))
				              
				            # else:
				            #     print("{0} is not a leap year".format(i.year))
				        else:
				            # print("{0} is a leap year".format(i.year))
				            obj.bisect_years_in_centuries+=(str(i.year)+ ", ")

				            count += 1
				    # else:
				    #     print("{0} is not a leap year".format(i.year))

				obj.bisect_years_count_in_centuries = count

				obj.used_in_calculations_by_user = True


				obj.save()

				form = BisectYearsinCenturiesForm()
	else:

		form = BisectYearsinCenturiesForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/bisect-years-in-centuries.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def how_many_months_and_days_till_the_next_spring_equinox(request):


	if request.method == 'POST':

		form = MonthsandDaystillthenextSpringEquinoxForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			d = obj.first_date_next_spring_equinox

			dt = obj.second_date_next_spring_equinox

			td = dt - d

			obj.days_until_next_spring_equinox = td.days

			obj.months_until_next_spring_equinox = td.days//30

			obj.used_in_calculations_by_user = True

			obj.save()

			form = MonthsandDaystillthenextSpringEquinoxForm()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form = MonthsandDaystillthenextSpringEquinoxForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/days-till-the-next-spring-equinox.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    



def how_many_months_and_days_till_the_next_autumn_equinox(request):


	if request.method == 'POST':

		form = MonthsandDaystillthenextAutumnEquinoxForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			d = obj.first_date_next_autumn_equinox

			dt = obj.second_date_next_autumn_equinox

			td = dt - d

			obj.days_until_next_autumn_equinox = td.days

			obj.months_until_next_autumn_equinox = td.days//30

			obj.used_in_calculations_by_user = True

			obj.save()

			form = MonthsandDaystillthenextAutumnEquinoxForm()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form = MonthsandDaystillthenextAutumnEquinoxForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/days-till-the-next-autumn-equinox.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    
    




def what_period_between_years_with_total_lunar_eclipse(request):


	if request.method == 'POST':

		form = PeriodsbetweenDateswithTotalLunarEclipseForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			res = []

			res_1 = []

			res_2 = []


			dt_le = [(obj.first_date_with_total_lunar_eclipse.year,
				obj.first_date_with_total_lunar_eclipse.month,
				obj.first_date_with_total_lunar_eclipse.day,)]

			dt_le_1= [(obj.second_date_with_total_lunar_eclipse.year,
				obj.second_date_with_total_lunar_eclipse.month,
				obj.second_date_with_total_lunar_eclipse.day,)]


			for i in range(1):


				if (obj.second_date_with_total_lunar_eclipse.month == 1 and 
					obj.second_date_with_total_lunar_eclipse.day == 1) :

					res.append(0)
					res_1.append(abs(12 - dt_le[i][1]))
					res_2.append(abs(30 - dt_le[i][2])+7)

				elif  (obj.first_date_with_total_lunar_eclipse.year !=  
					obj.second_date_with_total_lunar_eclipse.year) :

					res.append(0)
					res_1.append(dt_le_1[i][1]+ abs(12 - dt_le[i][1])-1)
					res_2.append(abs(30 - dt_le[i][2])+dt_le_1[i][2]+9)

				
				else:

					res.append(dt_le_1[i][0]- dt_le[i][0])
					res_1.append(abs(dt_le_1[i][1] - dt_le[i][1]))
					res_2.append(abs(dt_le_1[i][2] - dt_le[i][2]))


			

			td = timedelta(days=res[0]*365 + res_2[0]+ (res_1[0]*4*7))

			if (obj.second_date_with_total_lunar_eclipse.day <

			obj.first_date_with_total_lunar_eclipse.day  and  

			obj.first_date_with_total_lunar_eclipse.year !=  
				obj.second_date_with_total_lunar_eclipse.year):

				td = timedelta(days=res[0]*365 + res_2[0]+ (res_1[0]*4*7))


			elif (obj.second_date_with_total_lunar_eclipse.day <

				obj.first_date_with_total_lunar_eclipse.day
				and  obj.first_date_with_total_lunar_eclipse.year == 
				obj.second_date_with_total_lunar_eclipse.year) :

				td = td - timedelta(days=abs(int(obj.first_date_with_total_lunar_eclipse.day)-
					int(obj.second_date_with_total_lunar_eclipse.day)))



			else:

				td = td + timedelta(days=5)




			print(str(obj.second_date_with_total_lunar_eclipse.month))
			print(str(obj.second_date_with_total_lunar_eclipse.day))

			print("days",td.days)
			print(res)
			print(res_1)
			print(res_2)


			obj.months_between_dates_with_total_lunar_eclipse = td.days//30
			obj.minutes_between_dates_with_total_lunar_eclipse = td.days * 1440

			obj.used_in_calculations_by_user = True

			obj.save()

			form = PeriodsbetweenDateswithTotalLunarEclipseForm()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form = PeriodsbetweenDateswithTotalLunarEclipseForm()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/periods-between-dates-with-total-lunar-eclipse.html"

	return render(request, template_path, {'form': form, "obj":obj, })







def find_the_equivalent_of_timezone_with_USA(request):


	if request.method == 'POST':

		form = Find_the_equivalent_of_timezone_with_USA_Form(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			inTimeDelta = datetime.timedelta(hours=obj.inTimeDelta_hours)

			inTZObject = datetime.timezone(inTimeDelta, obj.inTZObject_name)

			obj.datetime_instance_var = datetime.datetime(obj.datetime_instance_var.year,
			obj.datetime_instance_var.month, obj.datetime_instance_var.day, 
			obj.datetime_instance_var.hour, obj.datetime_instance_var.minute, 
			obj.datetime_instance_var.second, obj.datetime_instance_var.microsecond,
			 inTZObject)


			if obj.inTimeDelta_hours < 1:

				var  =  (obj.datetime_instance_var - obj.datetime_instance_var.utcoffset())

				obj.first_date_time_var = inTZObject.fromutc(var)

				obj.second_date_time_var = inTZObject.fromutc(obj.datetime_instance_var)

			else:

				obj.first_date_time_var = inTZObject.fromutc(obj.datetime_instance_var)

				var  =  (obj.datetime_instance_var - obj.datetime_instance_var.utcoffset())

				obj.second_date_time_var = inTZObject.fromutc(var)


			obj.used_in_calculations_by_user = True

			obj.save()

			form = Find_the_equivalent_of_timezone_with_USA_Form()

	else:

		form = Find_the_equivalent_of_timezone_with_USA_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/find-the-equivalent-of-timezone-with-USA.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    

	


def find_the_difference_of_timezone_with_USA(request):


	if request.method == 'POST':

		form = Find_the_difference_of_timezone_with_USA_Form(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			USANYTimeDelta = datetime.timedelta(hours=obj.inTimeDelta_hours_diff)

			USANYTZObject= datetime.timezone(USANYTimeDelta, obj.inTZObject_name_diff)

			obj.datetime_instance_var_diff = datetime.datetime(obj.datetime_instance_var_diff.year,
			obj.datetime_instance_var_diff.month, obj.datetime_instance_var_diff.day, 
			obj.datetime_instance_var_diff.hour, obj.datetime_instance_var_diff.minute, 
			obj.datetime_instance_var_diff.second, obj.datetime_instance_var_diff.microsecond,
			USANYTZObject)


			if obj.inTimeDelta_hours_diff < 1:



				obj.first_date_time_var_diff = USANYTZObject.fromutc(obj.datetime_instance_var_diff)

				var  =  (obj.datetime_instance_var_diff - obj.datetime_instance_var_diff.utcoffset())

				obj.second_date_time_var_diff = USANYTZObject.fromutc(var)


			else:

				var  =  (obj.datetime_instance_var_diff - obj.datetime_instance_var_diff.utcoffset())

				obj.first_date_time_var_diff = USANYTZObject.fromutc(var)

				obj.second_date_time_var_diff = USANYTZObject.fromutc(obj.datetime_instance_var_diff)




			obj.timezone_diff_days = obj.datetime_instance_var_diff.utcoffset().days

			obj.timezone_diff_minutes =  abs(obj.datetime_instance_var_diff.utcoffset()).seconds // 60

			obj.used_in_calculations_by_user = True

			obj.save()

			form = Find_the_difference_of_timezone_with_USA_Form()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form = Find_the_difference_of_timezone_with_USA_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/find-the-difference-of-timezone-with-USA.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    

	



def display_calculators_page_view(request):

	return render(request, 'Days/page-with-calculators.html')






def find_equivalent_with_timezone(request):

	if request.method == 'POST':

		form = Find_equivalent_with_timezone_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			inTimeDelta = datetime.timedelta(hours=obj.inTimeDelta_hours)

			inTZObject = datetime.timezone(inTimeDelta, str(obj.inTZObject_name_field))

			obj.datetime_instance_var = datetime.datetime(obj.datetime_instance_var.year,
			obj.datetime_instance_var.month, obj.datetime_instance_var.day, 
			obj.datetime_instance_var.hour, obj.datetime_instance_var.minute, 
			obj.datetime_instance_var.second, obj.datetime_instance_var.microsecond,
			 inTZObject)


			if obj.inTimeDelta_hours < 1:

				var  =  (obj.datetime_instance_var - obj.datetime_instance_var.utcoffset())

				obj.first_date_time_var = inTZObject.fromutc(var)

				obj.second_date_time_var = inTZObject.fromutc(obj.datetime_instance_var)

			else:

				obj.first_date_time_var = inTZObject.fromutc(obj.datetime_instance_var)

				var  =  (obj.datetime_instance_var - obj.datetime_instance_var.utcoffset())

				obj.second_date_time_var = inTZObject.fromutc(var)


			obj.used_in_calculations_by_user = True

			obj.save()

			form =  Find_equivalent_with_timezone_Form()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form =  Find_equivalent_with_timezone_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/find-equivalent-with-timezone.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    


	

def find_difference_with_timezone(request):

	if request.method == 'POST':

		form = Find_difference_with_timezone_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			inTimeDelta = datetime.timedelta(hours=obj.inTimeDelta_hours_diff)

			inTZObject = datetime.timezone(inTimeDelta, str(obj.inTZObject_name_diff_filed))

			obj.datetime_instance_var_diff = datetime.datetime(obj.datetime_instance_var_diff.year,
			obj.datetime_instance_var_diff.month, obj.datetime_instance_var_diff.day, 
			obj.datetime_instance_var_diff.hour, obj.datetime_instance_var_diff.minute, 
			obj.datetime_instance_var_diff.second, obj.datetime_instance_var_diff.microsecond,
			 inTZObject)


			if obj.inTimeDelta_hours_diff < 1:

				var  =  (obj.datetime_instance_var_diff - obj.datetime_instance_var_diff.utcoffset())

				obj.first_date_time_var_diff = inTZObject.fromutc(var)

				obj.second_date_time_var_diff = inTZObject.fromutc(obj.datetime_instance_var_diff)

			else:

				obj.first_date_time_var_diff = inTZObject.fromutc(obj.datetime_instance_var_diff)

				var  =  (obj.datetime_instance_var_diff - obj.datetime_instance_var_diff.utcoffset())

				obj.second_date_time_var_diff = inTZObject.fromutc(var)



			obj.timezone_diff_days = obj.datetime_instance_var_diff.utcoffset().days

			obj.timezone_diff_minutes =  abs(obj.datetime_instance_var_diff.utcoffset()).seconds // 60


			obj.used_in_calculations_by_user = True

			obj.save()

			form =  Find_difference_with_timezone_Form()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form =  Find_difference_with_timezone_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/find-difference-with-timezone.html"
	return render(request, template_path, {'form': form, "obj":obj, })

    






def find_difference_of_timezone_from_UTC(request):

	if request.method == 'POST':

		form = Find_difference_of_timezone_from_UTC_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			geolocator = Nominatim(user_agent="TimeApp")

			location = geolocator.geocode(str(obj.your_address))

			latitude_longitude = (location.latitude, location.longitude)

			if "address" in request.POST:

				if int(latitude_longitude[1]) in range( -165, -180, -1):
					obj.inTimeDelta_hours = -11
				elif int(latitude_longitude[1]) in range( -150, -165, -1):
					obj.inTimeDelta_hours = -10
				elif int(latitude_longitude[1]) in range( -135, -150, -1):
					obj.inTimeDelta_hours = -9
				elif int(latitude_longitude[1]) in range( -120, -135, -1):
					obj.inTimeDelta_hours = -8
				elif int(latitude_longitude[1]) in range( -105, -120, -1):
					obj.inTimeDelta_hours = -7
				elif int(latitude_longitude[1]) in range( -90, -105, -1):
					obj.inTimeDelta_hours = -6
				elif int(latitude_longitude[1]) in range( -75, -90, -1):
					obj.inTimeDelta_hours = -5
				elif int(latitude_longitude[1]) in range( -60, -75, -1):
					obj.inTimeDelta_hours = -4
				
				elif int(latitude_longitude[1]) in range( -45, -60,-1):
					obj.inTimeDelta_hours = -3
				elif int(latitude_longitude[1]) in range( -30, -45,-1):
					obj.inTimeDelta_hours = -2
				elif int(latitude_longitude[1]) in range(-15, -30, -1):
					obj.inTimeDelta_hours = -1
				elif int(latitude_longitude[1]) in range(0,-15 -1):
					obj.inTimeDelta_hours = 12
				elif int(latitude_longitude[1]) in range(0, 15):
					obj.inTimeDelta_hours = 1
				elif int(latitude_longitude[1]) in range(15, 30):
					obj.inTimeDelta_hours = 2
				elif int(latitude_longitude[1]) in range(30, 45):
					obj.inTimeDelta_hours = 3
				elif int(latitude_longitude[1]) in range(45, 60):
					obj.inTimeDelta_hours = 4
				

				elif int(latitude_longitude[1]) in range(60, 75):
					obj.inTimeDelta_hours = 5
				elif int(latitude_longitude[1]) in range(75, 90):
					obj.inTimeDelta_hours = 6
				elif int(latitude_longitude[1]) in range(90, 105):
					obj.inTimeDelta_hours = 7
				elif int(latitude_longitude[1]) in range(105, 120):
					obj.inTimeDelta_hours = 8
				elif int(latitude_longitude[1]) in range(120, 135):
					obj.inTimeDelta_hours = 9
				elif int(latitude_longitude[1]) in range(135, 150):
					obj.inTimeDelta_hours = 10
				elif int(latitude_longitude[1]) in range(150, 165):
					obj.inTimeDelta_hours = 11
				elif int(latitude_longitude[1]) in range(165, 180):
					obj.inTimeDelta_hours = 12
				
			

			print(latitude_longitude)

			print("inTimeDelta_hours", obj.inTimeDelta_hours)
			

			inTimeDelta = datetime.timedelta(hours=obj.inTimeDelta_hours)

			inTZObject = datetime.timezone(inTimeDelta, str(obj.inTZObject_name_field))

			obj.datetime_instance_var = datetime.datetime(obj.datetime_instance_var.year,
			obj.datetime_instance_var.month, obj.datetime_instance_var.day, 
			obj.datetime_instance_var.hour, obj.datetime_instance_var.minute, 
			obj.datetime_instance_var.second, obj.datetime_instance_var.microsecond,
			 inTZObject)


			if obj.inTimeDelta_hours < 1:

				var  =  (obj.datetime_instance_var - obj.datetime_instance_var.utcoffset())

				obj.first_date_time_var = inTZObject.fromutc(var)

				obj.second_date_time_var = inTZObject.fromutc(obj.datetime_instance_var)

			else:

				obj.first_date_time_var = inTZObject.fromutc(obj.datetime_instance_var)

				var  =  (obj.datetime_instance_var - obj.datetime_instance_var.utcoffset())

				obj.second_date_time_var = inTZObject.fromutc(var)



			obj.used_in_calculations_by_user = True

			obj.save()

			form = Find_difference_of_timezone_from_UTC_Form()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form = Find_difference_of_timezone_from_UTC_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/difference-of-timezone-from-UTC.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    

	




def find_difference_between_two_timezones(request):

	if request.method == 'POST':

		form = find_difference_between_two_timezones_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			geolocator = Nominatim(user_agent="TimeApp")

			location = geolocator.geocode(str(obj.your_address))

			location_to_search = geolocator.geocode(str(obj.address_to_search))

			latitude_longitude = (location.latitude, location.longitude)

			latitude_longitude_to_search = (location_to_search.latitude, 
				location_to_search.longitude)


			if "address" in request.POST:

				if int(latitude_longitude[1]) in range( -165, -180, -1):
					obj.inTimeDelta_hours = -11
				elif int(latitude_longitude[1]) in range( -150, -165, -1):
					obj.inTimeDelta_hours = -10
				elif int(latitude_longitude[1]) in range( -135, -150, -1):
					obj.inTimeDelta_hours = -9
				elif int(latitude_longitude[1]) in range( -120, -135, -1):
					obj.inTimeDelta_hours = -8
				elif int(latitude_longitude[1]) in range( -105, -120, -1):
					obj.inTimeDelta_hours = -7
				elif int(latitude_longitude[1]) in range( -90, -105, -1):
					obj.inTimeDelta_hours = -6
				elif int(latitude_longitude[1]) in range( -75, -90, -1):
					obj.inTimeDelta_hours = -5
				elif int(latitude_longitude[1]) in range( -60, -75, -1):
					obj.inTimeDelta_hours = -4
				
				elif int(latitude_longitude[1]) in range( -45, -60,-1):
					obj.inTimeDelta_hours = -3
				elif int(latitude_longitude[1]) in range( -30, -45,-1):
					obj.inTimeDelta_hours = -2
				elif int(latitude_longitude[1]) in range(-15, -30, -1):
					obj.inTimeDelta_hours = -1
				elif int(latitude_longitude[1]) in range(0,-15 -1):
					obj.inTimeDelta_hours = 12
				elif int(latitude_longitude[1]) in range(0, 15):
					obj.inTimeDelta_hours = 1
				elif int(latitude_longitude[1]) in range(15, 30):
					obj.inTimeDelta_hours = 2
				elif int(latitude_longitude[1]) in range(30, 45):
					obj.inTimeDelta_hours = 3
				elif int(latitude_longitude[1]) in range(45, 60):
					obj.inTimeDelta_hours = 4
				

				elif int(latitude_longitude[1]) in range(60, 75):
					obj.inTimeDelta_hours = 5
				elif int(latitude_longitude[1]) in range(75, 90):
					obj.inTimeDelta_hours = 6
				elif int(latitude_longitude[1]) in range(90, 105):
					obj.inTimeDelta_hours = 7
				elif int(latitude_longitude[1]) in range(105, 120):
					obj.inTimeDelta_hours = 8
				elif int(latitude_longitude[1]) in range(120, 135):
					obj.inTimeDelta_hours = 9
				elif int(latitude_longitude[1]) in range(135, 150):
					obj.inTimeDelta_hours = 10
				elif int(latitude_longitude[1]) in range(150, 165):
					obj.inTimeDelta_hours = 11
				elif int(latitude_longitude[1]) in range(165, 180):
					obj.inTimeDelta_hours = 12
				
			#########################################################################	#####################################################################
			



				if int(latitude_longitude_to_search[1]) in range( -165, -180, -1):
					obj.inTimeDelta_hours_to_search = -11
				elif int(latitude_longitude_to_search[1]) in range( -150, -165, -1):
					obj.inTimeDelta_hours_to_search = -10
				elif int(latitude_longitude_to_search[1]) in range( -135, -150, -1):
					obj.inTimeDelta_hours_to_search = -9
				elif int(latitude_longitude_to_search[1]) in range( -120, -135, -1):
					obj.inTimeDelta_hours_to_search = -8
				elif int(latitude_longitude_to_search[1]) in range( -105, -120, -1):
					obj.inTimeDelta_hours_to_search = -7
				elif int(latitude_longitude_to_search[1]) in range( -90, -105, -1):
					obj.inTimeDelta_hours_to_search = -6
				elif int(latitude_longitude_to_search[1]) in range( -75, -90, -1):
					obj.inTimeDelta_hours_to_search = -5
				elif int(latitude_longitude_to_search[1]) in range( -60, -75, -1):
					obj.inTimeDelta_hours_to_search = -4
				
				elif int(latitude_longitude_to_search[1]) in range( -45, -60,-1):
					obj.inTimeDelta_hours_to_search = -3
				elif int(latitude_longitude_to_search[1]) in range( -30, -45,-1):
					obj.inTimeDelta_hours_to_search = -2
				elif int(latitude_longitude_to_search[1]) in range(-15, -30, -1):
					obj.inTimeDelta_hours_to_search = -1
				elif int(latitude_longitude_to_search[1]) in range(0,-15 -1):
					obj.inTimeDelta_hours_to_search = 12
				elif int(latitude_longitude_to_search[1]) in range(0, 15):
					obj.inTimeDelta_hours_to_search = 1
				elif int(latitude_longitude_to_search[1]) in range(15, 30):
					obj.inTimeDelta_hours_to_search = 2
				elif int(latitude_longitude_to_search[1]) in range(30, 45):
					obj.inTimeDelta_hours_to_search = 3
				elif int(latitude_longitude_to_search[1]) in range(45, 60):
					obj.inTimeDelta_hours_to_search = 4
				

				elif int(latitude_longitude_to_search[1]) in range(60, 75):
					obj.inTimeDelta_hours_to_search = 5
				elif int(latitude_longitude_to_search[1]) in range(75, 90):
					obj.inTimeDelta_hours_to_search = 6
				elif int(latitude_longitude_to_search[1]) in range(90, 105):
					obj.inTimeDelta_hours_to_search = 7
				elif int(latitude_longitude_to_search[1]) in range(105, 120):
					obj.inTimeDelta_hours_to_search = 8
				elif int(latitude_longitude_to_search[1]) in range(120, 135):
					obj.inTimeDelta_hours_to_search = 9
				elif int(latitude_longitude_to_search[1]) in range(135, 150):
					obj.inTimeDelta_hours_to_search = 10
				elif int(latitude_longitude_to_search[1]) in range(150, 165):
					obj.inTimeDelta_hours_to_search = 11
				elif int(latitude_longitude_to_search[1]) in range(165, 180):
					obj.inTimeDelta_hours_to_search = 12






			print(latitude_longitude)

			print("inTimeDelta_hours", obj.inTimeDelta_hours)

			obj.inTimeDelta_hours_res = abs(obj.inTimeDelta_hours - obj.inTimeDelta_hours_to_search)
			

			obj.used_in_calculations_by_user = True

			obj.save()

			form = find_difference_between_two_timezones_Form()

			# return render(request, "Days/days-till-a-date.html")
	else:

		form = find_difference_between_two_timezones_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/difference-between-two-timezones.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    




def display_date_for_the_next_n_days(request):


	if request.method == 'POST':

		form = display_date_for_the_next_n_days_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			if ((obj.month_for_date_n_days >= 1 and obj.month_for_date_n_days <= 12) and
				(obj.n_days >=1  and obj.n_days<=30) and obj.year_for_date_n_days > 0):


				dl =[]

				dl_aux = []

				#dt_obj = date(2020, 10, 25)
				dt_obj = timezone.now()

				obj.pivot_value = dt_obj.day

				if (obj.month_for_date_n_days == 4 or obj.month_for_date_n_days==6 

				or obj.month_for_date_n_days == 9 or obj.month_for_date_n_days==11):

					if obj.pivot_value > obj.n_days:

						if ((obj.n_days+obj.pivot_value) > 30):



							for i in range(obj.pivot_value, obj.n_days+obj.pivot_value+1 - ((obj.n_days+obj.pivot_value)-30)):


								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))


							for i in range(1, ((obj.n_days+obj.pivot_value)-30)):

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days+1, i))

							

						elif ((obj.n_days+obj.pivot_value) <= 30):
						
							for i in range(obj.pivot_value, obj.pivot_value+obj.n_days):

								print(i)

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))

					else:

				


						if ((obj.n_days+obj.pivot_value) > 30) :

							for i in range(obj.pivot_value, obj.n_days+obj.pivot_value+1 - ((obj.n_days+obj.pivot_value)-30)):


								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))


							for i in range(1, ((obj.n_days+obj.pivot_value)-30)):

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days+1, i))

						
						elif ((obj.n_days+obj.pivot_value) <= 30):
						
							for i in range(obj.pivot_value, obj.pivot_value+obj.n_days):

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))





				elif obj.month_for_date_n_days == 2:

					if obj.pivot_value > obj.n_days:

						if ((obj.n_days+obj.pivot_value) > 28):



							for i in range(obj.pivot_value, obj.n_days+obj.pivot_value+1 - ((obj.n_days+obj.pivot_value)-28)):


								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))


							for i in range(1, ((obj.n_days+obj.pivot_value)-28)):

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days+1, i))

							

						elif ((obj.n_days+obj.pivot_value) <= 28):

						
							for i in range(obj.pivot_value, obj.pivot_value+obj.n_days):

								print(i)

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))

					else:

				


						if ((obj.n_days+obj.pivot_value) > 28) :

							for i in range(obj.pivot_value, obj.n_days+obj.pivot_value+1 - ((obj.n_days+obj.pivot_value)-28)):


								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))


							for i in range(1, ((obj.n_days+obj.pivot_value)-28)):

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days+1, i))

						
						elif ((obj.n_days+obj.pivot_value) <= 28):
						
							for i in range(obj.pivot_value, obj.pivot_value+obj.n_days):
						
								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))


				elif (obj.month_for_date_n_days == 1 or obj.month_for_date_n_days==3 or
				obj.month_for_date_n_days==5 or obj.month_for_date_n_days==7 
				or obj.month_for_date_n_days==8 or obj.month_for_date_n_days==10 or obj.month_for_date_n_days==12):
												
					if obj.pivot_value > obj.n_days:

						if ((obj.n_days+obj.pivot_value) > 31):



							for i in range(obj.pivot_value, obj.n_days+obj.pivot_value+1 - ((obj.n_days+obj.pivot_value)-31)):


								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))


							for i in range(1, ((obj.n_days+obj.pivot_value)-31)):

								if obj.month_for_date_n_days == 12:

									dl.append(date(1, 1, i))

								else:

									dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days+1, i))



						elif ((obj.n_days+obj.pivot_value) <= 31):
						
							for i in range(obj.pivot_value, obj.pivot_value+obj.n_days):

								print(i)

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))

					else:

				


						if ((obj.n_days+obj.pivot_value) > 31) :

							for i in range(obj.pivot_value, obj.n_days+obj.pivot_value+1 - ((obj.n_days+obj.pivot_value)-31)):


								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))


							for i in range(1, ((obj.n_days+obj.pivot_value)-31)):

								if obj.month_for_date_n_days == 12:

									dl.append(date(1, 1, i))

								else:

									dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days+1, i))



						
						elif ((obj.n_days+obj.pivot_value) <= 31):
						
							for i in range(obj.pivot_value, obj.pivot_value+obj.n_days):

								dl.append(date(obj.year_for_date_n_days, obj.month_for_date_n_days, i))
				


				obj.date_for_the_next_n_days = " "

				for i in dl:

					obj.date_for_the_next_n_days+=str(i) 
					obj.date_for_the_next_n_days += "\n" 


				obj.used_in_calculations_by_user = True

				obj.save()

				form = display_date_for_the_next_n_days_Form()

				# return render(request, "Days/days-till-a-date.html")

	
	else:

		form = display_date_for_the_next_n_days_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/date-for-the-next-n-days.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def find_dates_with_attributes_of_time_equal_to_date_in_a_decade(request):

	if request.method == 'POST':

		form = attributes_of_time_equal_to_date_in_a_decade_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			if (((obj.second_year_in_a_decade_sum_attributes - obj.first_year_in_a_decade_sum_attributes) == 10)

				and (obj.month_sum_attributes >= 1 and obj.month_sum_attributes <=12 ) and 

				(obj.day_sum_attributes >=1 and obj.day_sum_attributes <= 30)):


				dl =[]

				dtl =[]

				dti = []


				for i in range(obj.first_year_in_a_decade_sum_attributes, obj.second_year_in_a_decade_sum_attributes+1):

					dl.append(datetime.datetime(i, obj.month_sum_attributes, obj.day_sum_attributes))



				# print(dl)

				# print('\n')



				# dt_obj = timezone.now()


				for i in dl:

				    dtl.append(i.replace(hour=obj.hour_sum_attributes, minute=obj.minute_sum_attributes,
				     second=obj.second_sum_attributes))


				dates_sum_attributes_result = " "


				for i in dtl:

   					if (sum(map(int, str(i.year))) + i.month + i.day == i.hour + i.minute + i.second):

   						obj.dates_sum_attributes_result += str(i) + ", "

				for i in dtl:

   					print(sum(map(int, str(i.year))) + i.month + i.day == i.hour + i.minute + i.second)

				
				print("List", obj.dates_sum_attributes_result)

				obj.used_in_calculations_by_user = True

				obj.save()

				form = attributes_of_time_equal_to_date_in_a_decade_Form()

				# return render(request, "Days/days-till-a-date.html")



	
	else:

		form = attributes_of_time_equal_to_date_in_a_decade_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/attributes-of-time-equal-to-date.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def find_dates_with_attributes_of_time_equal_to_date_in_a_century(request):

	if request.method == 'POST':

		form = attributes_of_time_equal_to_date_in_a_century_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			if (((obj.second_year_in_a_century_sum_attributes - obj.first_year_in_a_century_sum_attributes) == 100)

				and (obj.month_sum_attributes_in_a_century >= 1 and obj.month_sum_attributes_in_a_century <=12 ) and 

				(obj.day_sum_attributes_in_a_century >=1 and obj.day_sum_attributes_in_a_century <= 30)):


				dl =[]

				dtl =[]

				dti = []


				for i in range(obj.first_year_in_a_century_sum_attributes, obj.second_year_in_a_century_sum_attributes+1):

					dl.append(datetime.datetime(i, obj.month_sum_attributes_in_a_century, obj.day_sum_attributes_in_a_century))



				# print(dl)

				# print('\n')



				# dt_obj = timezone.now()


				for i in dl:

				    dtl.append(i.replace(hour=obj.hour_sum_attributes_in_a_century, minute=obj.minute_sum_attributes_in_a_century,
				     second=obj.second_sum_attributes_in_a_century))


				dates_sum_attributes_result = " "


				for i in dtl:

   					if (sum(map(int, str(i.year))) + i.month + i.day == i.hour + i.minute + i.second):

   						obj.dates_sum_attributes_in_a_century_result += str(i) + ", "

				for i in dtl:

   					print(sum(map(int, str(i.year))) + i.month + i.day == i.hour + i.minute + i.second)

				
				print("List", obj.dates_sum_attributes_in_a_century_result)

				obj.used_in_calculations_by_user = True

				obj.save()

				form = attributes_of_time_equal_to_date_in_a_century_Form()

				# return render(request, "Days/days-till-a-date.html")

	else:

		form = attributes_of_time_equal_to_date_in_a_century_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/attributes-of-time-equal-to-date-in-a-century.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def find_time_until_a_date_after_n_years(request):


	if request.method == 'POST':

		form = find_time_until_a_date_after_n_years_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			if obj.nth_day_time_until <= 30:


				dt=timezone.now()


				dt_obj=dt.replace(year=dt.year+obj.n_years_time_until, day=obj.nth_day_time_until)

				obj.first_date_time_until = dt

				obj.second_date_time_until = dt_obj

				print(dt)

				print(dt_obj)

				td = dt_obj -dt

				tdh = td.days * 24

				tdm = tdh*60

				tds = tdh*3600

				obj.days_until_result=td.days

				print(td.days)

				print(tdh,'hours',tdh*60, 'minutes', tdh*3600, 'seconds')

				obj.time_until_result = " "

				obj.time_until_result += str(tdh)+ " hours "+str(tdm)+" minutes "+str(tds)+" seconds "


				obj.used_in_calculations_by_user = True

				obj.save()

				form = find_time_until_a_date_after_n_years_Form()

				# return render(request, "Days/days-till-a-date.html")

	else:

		form = find_time_until_a_date_after_n_years_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/time-until-a-date-after-n-years.html"

	return render(request, template_path, {'form': form, "obj":obj, })







def calculate_date_and_time_until_next_solstice(request):


	if request.method == 'POST':

		form = calculate_date_and_time_until_next_solstice_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			dt = timezone.now() 

			dt_obj = dt.replace(day=obj.next_solstice.day, month=obj.next_solstice.month)

			td = dt_obj - dt

			td_d = td.days

			td_h = td.days * 24

			td_m = td_h*60

			td_s = td_h*3600

			obj.days_until_solstice = td.days

			print(td_d,'days', td_h, 'hours', td_h * 60, 'minutes', td_h*3600, 'seconds')

			obj.date_and_time_until_solstice = " "

			obj.date_and_time_until_solstice += str(td_h)+ " hours "+str(td_m)+" minutes "+str(td_s)+" seconds "

			obj.used_in_calculations_by_user = True

			obj.save()

			form = calculate_date_and_time_until_next_solstice_Form()

			# return render(request, "Days/days-till-a-date.html")

	else:

		form = calculate_date_and_time_until_next_solstice_Form()

	obj = Day.objects.last()

	# context_dictionary = {'form' : form,}

	template_path = "Days/date-and-time-until-next-solstice.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def calculate_date_and_time_until_the_nth_day_in_the_next_n_years(request):

		if request.method == 'POST':

			form = date_and_time_until_the_nth_day_in_the_next_n_years_Form(request.POST)

			if form.is_valid():

				form.save()

				obj = Day.objects.last()


				dli = []

				dtl =[]

				dt = datetime_function.now()

				# datetime_function.now(tz=tzinfo_class.utc)

				# obj.year_one_next_n_years = 2021

				# obj.year_two_next_n_years = 2033


				for i in range(obj.year_one_next_n_years+1, obj.year_two_next_n_years+1):
				    dli.append(datetime_function(i, obj.month_next_n_years, obj.day_next_n_years))


				print(dli)

				print('\n')


				for i in dli:
				    dtl.append(i.replace(hour=dt.hour, minute=dt.minute, second=dt.second))


				# print(dtl)

				# print('\n')



				for i in dtl:
				    print(i - dt)


				obj.date_and_time_until_nth_day_in_the_next_n_years = " "

				for i in dtl:

					obj.date_and_time_until_nth_day_in_the_next_n_years += str(i-dt) + ", "


				obj.used_in_calculations_by_user = True

				obj.save()

				form = date_and_time_until_the_nth_day_in_the_next_n_years_Form()

				# return render(request, "Days/days-till-a-date.html")

		else:

			form = date_and_time_until_the_nth_day_in_the_next_n_years_Form()

		obj = Day.objects.last()

		# context_dictionary = {'form' : form,}

		template_path = "Days/date-and-time-until-the-nth-day-in-the-next-n-years.html"

		return render(request, template_path, {'form': form, "obj":obj, })


    



def find_which_years_of_nth_century_have_more_than_n_days_with_attrs(request):


	if request.method == 'POST':

			form = years_of_nth_century_have_more_than_n_days_with_attrs_Form(request.POST)

			if form.is_valid():

				form.save()

				obj = Day.objects.last()

				if ((obj.first_year_of_nth_century_attributes > 0 and
				obj.second_year_of_nth_century_attributes > 0) and 
				(obj.second_year_of_nth_century_attributes - obj.first_year_of_nth_century_attributes) == 100):

					dtl=[]

					dti =[]

					yl = []



					for i in range(obj.first_year_of_nth_century_attributes, 
						obj.second_year_of_nth_century_attributes):
					    for m in range(1, 13):
					        if m==4 or m==6 or m==9 or m==11:
					            for j in range(1, 31):
					                dtl.append(datetime_function(i, m, j))
					        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
					            for j in range(1, 32):
					                dtl.append(datetime_function(i, m, j))
					        else:
					            for j in range(1, 29):
					                dtl.append(datetime_function(i, m, j))


					dt_obj = datetime_function.now()


					for i in dtl:

					    dti.append(i.replace(hour=dt_obj.hour, minute=dt_obj.minute, second=dt_obj.second))

					print(dti)

					for i in dti:

						if (sum(map(int, str(i.year))) + i.month + i.day == i.hour + i.minute + i.second):

							print('Match found:', i)



							yl.append(i.year)


					for i in yl:

						print(i, yl.count(i))

					obj.n_days_attributes_result = " "


					for i in yl:

						obj.n_days_attributes_result+=str(i) +": " + str(yl.count(i))+ ", "



					obj.n_days_attributes = len(yl)
						

					obj.used_in_calculations_by_user = True

					obj.save()

					form = years_of_nth_century_have_more_than_n_days_with_attrs_Form()
	else:

		form = years_of_nth_century_have_more_than_n_days_with_attrs_Form()

	obj = Day.objects.last()

		# context_dictionary = {'form' : form,}

	template_path = "Days/years-of-nth-century-have-more-than-n-days-with-attrs.html"

	return render(request, template_path, {'form': form, "obj":obj, })


	    



def how_many_solstices_in_n_years_with_sum_attrs_even_number(request):

	if request.method == 'POST':

			form = solstices_in_n_years_with_sum_attrs_even_number_Form(request.POST)

			if form.is_valid():

				form.save()

				obj = Day.objects.last()

				if (obj.first_year_solstice_even_sum > 0 and obj.second_year_solstice_even_sum > 0):

					dt = datetime_function.now()

					dtl = []

					ssolsticel = []

					wsolsticel = []

					solsticel =[]

					sl =[]


					for i in range(obj.first_year_solstice_even_sum, obj.second_year_solstice_even_sum):
					    for m in range(1, 13):
					        if m==4 or m==6 or m==9 or m==11:
					            for j in range(1, 31):
					                dtl.append(datetime_function(i, m, j, dt.hour, dt.minute, dt.second))
					        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
					            for j in range(1, 32):
					                dtl.append(datetime_function(i, m, j, dt.hour, dt.minute, dt.second))
					        else:
					            for j in range(1, 29):
					                dtl.append(datetime_function(i, m, j, dt.hour, dt.minute, dt.second))
        


									
					for i in dtl:
					    if (i.day == 21 and i.month == 6):
					        ssolsticel.append(i)


					        

					for i in dtl:
					    if (i.day == 21 and i.month == 12):
					        wsolsticel.append(i)



					print('Summer solstices: ', ssolsticel)

					print('Winter solstices: ', wsolsticel)



					solsticel = ssolsticel + wsolsticel

					obj.ssolsticel_even_sum = " "

					obj.wsolsticel_even_sum = " "

					obj.solsticel_even_sum = " "


					for i in ssolsticel:

					     if ((sum(map(int, str(i.year))) + i.month + i.day + i.hour + i.minute + i.second) %2 == 0):

				         	obj.ssolsticel_even_sum+=str(i) + ", "

				         	obj.ssolsticel_even_sum_count+=1


					for i in wsolsticel:

						if ((sum(map(int, str(i.year))) + i.month + i.day + i.hour + i.minute + i.second) %2 == 0):

							obj.wsolsticel_even_sum+=str(i) + ", "

							obj.wsolsticel_even_sum_count += 1	


					for i in solsticel:

						if ((sum(map(int, str(i.year))) + i.month + i.day + i.hour + i.minute + i.second) %2 == 0):

							obj.solsticel_even_sum += str(i) + ", "

							obj.solsticel_even_sum_count += 1



					print(obj.ssolsticel_even_sum_count)
					print(obj.wsolsticel_even_sum_count)
					print(obj.solsticel_even_sum_count)



					obj.used_in_calculations_by_user = True

					obj.save()

					form = solstices_in_n_years_with_sum_attrs_even_number_Form()
	else:

		form = solstices_in_n_years_with_sum_attrs_even_number_Form()

	obj = Day.objects.last()

		# context_dictionary = {'form' : form,}

	template_path = "Days/solstices-in-n-years-with-sum-attrs-even-number.html"

	return render(request, template_path, {'form': form, "obj":obj, })







def how_many_solstices_in_n_years_with_sum_attrs_odd_number(request):

	if request.method == 'POST':

			form = solstices_in_n_years_with_sum_attrs_odd_number_Form(request.POST)

			if form.is_valid():

				form.save()

				obj = Day.objects.last()

				if (obj.first_year_solstice_odd_sum > 0 and obj.second_year_solstice_odd_sum > 0):

					dt = datetime_function.now()

					dtl = []

					ssolsticel = []

					wsolsticel = []

					solsticel =[]

					sl =[]


					for i in range(obj.first_year_solstice_odd_sum, obj.second_year_solstice_odd_sum):
					    for m in range(1, 13):
					        if m==4 or m==6 or m==9 or m==11:
					            for j in range(1, 31):
					                dtl.append(datetime_function(i, m, j, dt.hour, dt.minute, dt.second))
					        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
					            for j in range(1, 32):
					                dtl.append(datetime_function(i, m, j, dt.hour, dt.minute, dt.second))
					        else:
					            for j in range(1, 29):
					                dtl.append(datetime_function(i, m, j, dt.hour, dt.minute, dt.second))
        


									
					for i in dtl:
					    if (i.day == 21 and i.month == 6):
					        ssolsticel.append(i)


					        

					for i in dtl:
					    if (i.day == 21 and i.month == 12):
					        wsolsticel.append(i)



					print('Summer solstices: ', ssolsticel)

					print('Winter solstices: ', wsolsticel)



					solsticel = ssolsticel + wsolsticel

					obj.ssolsticel_odd_sum = " "

					obj.wsolsticel_odd_sum = " "

					obj.solsticel_odd_sum = " "


					for i in ssolsticel:

					     if ((sum(map(int, str(i.year))) + i.month + i.day + i.hour + i.minute + i.second) %2 != 0):

				         	obj.ssolsticel_odd_sum+=str(i) + ", "

				         	obj.ssolsticel_odd_sum_count+=1


					for i in wsolsticel:

						if ((sum(map(int, str(i.year))) + i.month + i.day + i.hour + i.minute + i.second) %2 != 0):

							obj.wsolsticel_odd_sum+=str(i) + ", "

							obj.wsolsticel_odd_sum_count += 1	


					for i in solsticel:

						if ((sum(map(int, str(i.year))) + i.month + i.day + i.hour + i.minute + i.second) %2 != 0):

							obj.solsticel_odd_sum += str(i) + ", "

							obj.solsticel_odd_sum_count += 1

					print(obj.ssolsticel_odd_sum_count)
					print(obj.wsolsticel_odd_sum_count)
					print(obj.solsticel_odd_sum_count)



					obj.used_in_calculations_by_user = True

					obj.save()

					form = solstices_in_n_years_with_sum_attrs_odd_number_Form()
	else:

		form = solstices_in_n_years_with_sum_attrs_odd_number_Form()

	obj = Day.objects.last()

		# context_dictionary = {'form' : form,}

	template_path = "Days/solstices-in-n-years-with-sum-attrs-odd-number.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def view_calendar(request):


	if request.method == 'POST':

		form = view_calendar_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			dtl = []


			print("date",obj.date_one_calendar.year)

			# if obj.date_two_calendar.year == obj.date_one_calendar.year:

			#     for m in range(obj.date_one_calendar.month, obj.date_two_calendar.month+1):


			#         if m==4 or m==6 or m==9 or m==11:
			#             for j in range(1, 31):
			#                 dtl.append(date(obj.date_one_calendar.year, m, j))
			#         elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
			#             for j in range(1, 32):
			#                 dtl.append(date(obj.date_one_calendar.year, m, j))
			#         else:
			#             for j in range(1, 29):
			#                 dtl.append(date(obj.date_one_calendar.year, m, j))


			       

			# else:

			# 	for i in range(int(obj.date_one_calendar.year), int(obj.date_two_calendar.year)+1):  #2101  2201
			# 	    for m in range(1, 13):
			# 	    # for m in range(obj.date_one_calendar.month, obj.date_two_calendar.month+1):
			# 	        if m==4 or m==6 or m==9 or m==11:
			# 	            for j in range(1, 31):
			# 	                dtl.append(date(i, m, j))
			# 	        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
			# 	            for j in range(1, 32):
			# 	                dtl.append(date(i, m, j))
			# 	        else:
			# 	            for j in range(1, 29):
			# 	                dtl.append(date(i, m, j))





			if obj.date_two_calendar.year == obj.date_one_calendar.year:

				monthvar = obj.date_one_calendar.month


				if monthvar==4 or monthvar==6 or monthvar==9 or monthvar==11:
					for j in range(obj.date_one_calendar.day, 31):
						dtl.append(date(obj.date_one_calendar.year, monthvar, j))


				elif (monthvar==1 or monthvar==3 or monthvar==5 or monthvar==7 or 
		        	monthvar==8 or monthvar==10 or monthvar==12):

					for j in range(obj.date_one_calendar.day, 32):

						dtl.append(date(obj.date_one_calendar.year, monthvar, j))

				else:

					for j in range(obj.date_one_calendar.day, 29):

						dtl.append(date(obj.date_one_calendar.year, monthvar, j))




				for m in range(obj.date_one_calendar.month+1, obj.date_two_calendar.month):


					if m==4 or m==6 or m==9 or m==11:
					    for j in range(1, 31):
					        dtl.append(date(obj.date_one_calendar.year, m, j))
					elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
					    for j in range(1, 32):
					        dtl.append(date(obj.date_one_calendar.year, m, j))
					else:
					    for j in range(1, 29):
					        dtl.append(date(obj.date_one_calendar.year, m, j))




				monthvar1 = obj.date_two_calendar.month


				if monthvar1==4 or monthvar1==6 or monthvar1==9 or monthvar1==11:
					for j in range(1, obj.date_one_calendar.day):
						dtl.append(date(obj.date_one_calendar.year, monthvar1, j))


				elif (monthvar1==1 or monthvar1==3 or monthvar1==5 or monthvar1==7 or 
		        	monthvar1==8 or monthvar1==10 or monthvar1==12):

					for j in range(1, obj.date_two_calendar.day):

						dtl.append(date(obj.date_one_calendar.year, monthvar1, j))

				else:

					for j in range(1, obj.date_two_calendar.day):

						dtl.append(date(obj.date_one_calendar.year, monthvar1, j))



			else:


				monthvar = obj.date_one_calendar.month


				if monthvar==4 or monthvar==6 or monthvar==9 or monthvar==11:
					for j in range(obj.date_one_calendar.day, 31):
						dtl.append(date(obj.date_one_calendar.year, monthvar, j))


				elif (monthvar==1 or monthvar==3 or monthvar==5 or monthvar==7 or 
		        	monthvar==8 or monthvar==10 or monthvar==12):

					for j in range(obj.date_one_calendar.day, 32):

						dtl.append(date(obj.date_one_calendar.year, monthvar, j))

				else:

					for j in range(obj.date_one_calendar.day, 29):

						dtl.append(date(obj.date_one_calendar.year, monthvar, j))



				for m in range(obj.date_one_calendar.month+1, 13):


					if m==4 or m==6 or m==9 or m==11:
					    for j in range(1, 31):
					        dtl.append(date(obj.date_one_calendar.year, m, j))
					elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
					    for j in range(1, 32):
					        dtl.append(date(obj.date_one_calendar.year, m, j))
					else:
					    for j in range(1, 29):
					        dtl.append(date(obj.date_one_calendar.year, m, j))





				for i in range(int(obj.date_one_calendar.year+1), int(obj.date_two_calendar.year)+1):  #2101  2201

					if i != obj.date_two_calendar.year:

					    for m in range(1, 13):
					    # for m in range(obj.date_one_calendar.month, obj.date_two_calendar.month+1):
					        if m==4 or m==6 or m==9 or m==11:
					            for j in range(1, 31):
					                dtl.append(date(i, m, j))
					        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
					            for j in range(1, 32):
					                dtl.append(date(i, m, j))
					        else:
					            for j in range(1, 29):
					                dtl.append(date(i, m, j))



				for m in range(1, obj.date_two_calendar.month):


					if m==4 or m==6 or m==9 or m==11:
					    for j in range(1, 31):
					        dtl.append(date(obj.date_two_calendar.year, m, j))
					elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
					    for j in range(1, 32):
					        dtl.append(date(obj.date_two_calendar.year, m, j))
					else:
					    for j in range(1, 29):
					        dtl.append(date(obj.date_two_calendar.year, m, j))



				monthvar1 = obj.date_two_calendar.month

				if monthvar1==4 or monthvar1==6 or monthvar1==9 or monthvar1==11:

					for j in range(1, obj.date_two_calendar.day):

						dtl.append(date(obj.date_two_calendar.year, monthvar1, j))


				elif (monthvar1==1 or monthvar1==3 or monthvar1==5 or monthvar1==7 or 
			        	monthvar1==8 or monthvar1==10 or monthvar1==12):

					for j in range(1, obj.date_two_calendar.day):

						dtl.append(date(obj.date_two_calendar.year, monthvar1, j))

				else:

					for j in range(1, obj.date_two_calendar.day):

						dtl.append(date(obj.date_two_calendar.year, monthvar1, j))




			obj.date_for_the_next_n_weeks = " "

			for i in dtl:

				obj.date_for_the_next_n_weeks+=str(i)+", " 
				obj.date_for_the_next_n_weeks += "\n" 


			obj.used_in_calculations_by_user = True

			obj.save()

			form = view_calendar_Form()

			# return render(request, "Days/days-till-a-date.html")

	
	else:

		form = view_calendar_Form()

	obj = Day.objects.last()
	
	# context_dictionary = {'form' : form,}

	template_path = "Days/calendar.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def  create_the_DaysInSearchEngine_17(request):


	if request.method == 'POST':

		form = create_Days_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = DaysInSearchEngine.objects.last()


			for i in range(obj.year_one_period, obj.year_two_period):  #2101  2201
			    for m in range(1, 7):
			        if m==4 or m==6 or m==9 or m==11:
			            for j in range(1, 31):
			            	obj1 = DaysInSearchEngine()
			            	obj1.date_field = datetime_function(i, m, j)
			            	obj1.year_one_period = obj.year_one_period
			            	obj1.year_two_period == obj.year_two_period
			            	obj1.save()

			        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
			            for j in range(1, 32):
			                obj1 = DaysInSearchEngine()
			                obj1.date_field = datetime_function(i, m, j)
			                obj1.year_one_period = obj.year_one_period
			                obj1.year_two_period == obj.year_two_period
			                obj1.save()

			        elif m==2:
		        		for j in range(1,29):
				        	obj1 = DaysInSearchEngine()
				        	obj1.date_field = datetime_function(i, m, j)
				        	obj1.year_one_period = obj.year_one_period
				        	obj1.year_two_period == obj.year_two_period
				        	obj1.save()

			        obj.save()

			        form = create_Days_Form()


	
	else:

		form =create_Days_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/DaysInSearchEngine.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })





def  create_the_DaysInSearchEngine_712(request):


	if request.method == 'POST':

		form = create_Days_712_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = DaysInSearchEngine.objects.last()


			for i in range(obj.year_one_period, obj.year_two_period):  #2101  2201
			    for m in range(7, 13):
			        if m==4 or m==6 or m==9 or m==11:
			            for j in range(1, 31):
			            	obj1 = DaysInSearchEngine()
			            	obj1.date_field = datetime_function(i, m, j)
			            	obj1.year_one_period = obj.year_one_period
			            	obj1.year_two_period == obj.year_two_period
			            	obj1.save()

			        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
			            for j in range(1, 32):
			                obj1 = DaysInSearchEngine()
			                obj1.date_field = datetime_function(i, m, j)
			                obj1.year_one_period = obj.year_one_period
			                obj1.year_two_period == obj.year_two_period
			                obj1.save()

			        elif m==2:
		        		for j in range(1,29):
				        	obj1 = DaysInSearchEngine()
				        	obj1.date_field = datetime_function(i, m, j)
				        	obj1.year_one_period = obj.year_one_period
				        	obj1.year_two_period == obj.year_two_period
				        	obj1.save()

			        obj.save()

			        form = create_Days_712_Form()


	
	else:

		form =create_Days_712_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/DaysInSearchEngine-712.html"

	else:

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	return render(request, template_path, {'form': form})# "obj":obj, })


		



def  delete_the_DaysInSearchEngine(request):


	if request.method == 'POST':

		form = delete_Days_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = DaysInSearchEngine.objects.last()

			obj_2 = DaysInSearchEngine.objects.all()

			for i in obj_2:


				if (i.year_one_period == obj.year_one_period or
				i.year_two_period == obj.year_two_period):  #2101  2201

				    i.delete()

			obj.save()

			form = delete_Days_Form()


	
	else:

		form =delete_Days_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/delete-DaysInSearchEngine.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })

			





def determine_visibility_of_stars(request):


	if request.method == 'POST':

		form = determine_visibility_Form(request.POST)

		if form.is_valid():

			form.save()


			# obj = DaysInSearchEngine.objects.last()

			# qs = DaysInSearchEngine.objects.all()

			# obj = Stars.objects.last()

			qs1 = Stars.objects.all()

			for i in qs1:


				# if (i.year_one_period == obj.year_one_period or
				# i.year_two_period == obj.year_two_period):  #2101  2201

			    i.aparent_magnitude = i.absolute_magnitude - (5 + 5*math.log10(1/i.distance_from_Earth))

			    i.save()


			form = determine_visibility_Form()


	
	else:

		form = determine_visibility_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/determine-visibility.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })






# def ref_magnitudes(request):


# 	if request.method == 'POST':

# 		form = ref_magnitudes_Form(request.POST)

# 		if form.is_valid():

# 			form.save()

# 			obj = DaysInSearchEngine.objects.first()

# 			qs = DaysInSearchEngine.objects.filter(id__gte=obj.id, id__lte=obj.id+93)

# 			qs1 = Stars.objects.all()

# 			for item in qs1:

# 				if item.aparent_magnitude < 6.5:

# 					print(item.name)

# 					for i in qs:

# 						i.stars += item.name + ", "
			
# 						i.save()


# 			form = ref_magnitudes_Form()

	
# 	else:

# 		form = ref_magnitudes_Form()

# 	if request.user.is_authenticated and request.user.is_staff:

# 		template_path = "Days/ref-magnitudes.html"

# 	else: 

# 		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
# 	return render(request, template_path, {'form': form})# "obj":obj, })








def ref_magnitudes(request):


	if request.method == 'POST':

		form = ref_magnitudes_Form(request.POST)

		if form.is_valid():

			form.save()

			obj = DaysInSearchEngine.objects.last()

			obj1 =  obj.first_id_ref_magnitudes

			obj2 = obj.second_id_ref_magnitudes 

			qs = DaysInSearchEngine.objects.filter(id__gte=obj1, id__lte=obj2)

			qs1 = Stars.objects.all()

			for i in qs:

				i.stars = " "

			for item in qs1:

				if item.aparent_magnitude < 6.5:

					print(item.name)

					for i in qs:

						i.stars += item.name + ", "
			
						i.save()


			form = ref_magnitudes_Form()

	
	else:

		form = ref_magnitudes_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/ref-magnitudes.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })







def determine_most_visible_periods(request):


	if request.method == 'POST':

		form = determine_most_visible_periods_Form(request.POST)

		if form.is_valid():

			form.save()

			print("strstr")

			# obj = DaysInSearchEngine.objects.first()

			# qs = DaysInSearchEngine.objects.filter(id__gte=obj.id, id__lte=obj.id+5)

			obj = DaysInSearchEngine.objects.last()

			obj1 =  obj.first_id_most_visible_periods

			obj2 = obj.second_id_most_visible_periods

			qs = DaysInSearchEngine.objects.filter(id__gte=obj1, id__lte=obj2)


			qs1 = Stars.objects.all()


			for i in qs:

				i.most_visible_periods = " "

			for item in qs1:

				# print("str")

				print(item.ascension+item.declination)

				if (item.ascension+item.declination  >= 59.06 and  

				item.ascension+item.declination <= 89.52):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()



				elif (item.ascension+item.declination  >= -9.97  and  

				item.ascension+item.declination <= -9.97):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()



				elif (item.ascension+item.declination  >= -46.17  and  

				item.ascension+item.declination <= -46.17):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -46.03  and  

				item.ascension+item.declination <= -46.03):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -46.1  and  

				item.ascension+item.declination <= -46.1):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()




				elif (item.ascension+item.declination  >= 12.57  and  

				item.ascension+item.declination <= 12.57):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -55.9  and  

				item.ascension+item.declination <= -55.9):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= 12.77  and  

				item.ascension+item.declination <= 12.77):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -50.29  and  

				item.ascension+item.declination <= -50.29):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -46.83  and  

				item.ascension+item.declination <= -46.83):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -9.94  and  

				item.ascension+item.declination <= -9.94):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "always" + ", "
			
						i.save()




				elif (item.ascension+item.declination  >= -1.29 and 
				 item.ascension+item.declination <= -0.07 ):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "october-february" + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= 20.49 and 

				item.ascension+item.declination <= 28.57):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "november-april" + ", "
			
						i.save()



				elif (item.ascension+item.declination >= -6.39 and 

				item.ascension+item.declination <=  12.18):

					print("strstrstr")

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "may-august" + ", "
			
						i.save()



				elif (item.ascension+item.declination  >= -14.13 
				and item.ascension+item.declination <= 14.12):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "february-may" + ", "
			
						i.save()




				elif (item.ascension+item.declination  >= 20.38 and 
				item.ascension+item.declination <= 27.45):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "august-february" + ", "
			
						i.save()




				elif (item.ascension+item.declination >= 30.89 and 
				item.ascension+item.declination <= 41.05):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "august-april" + ", "
			
						i.save()




				elif (item.ascension+item.declination >= 42 and 
				item.ascension+item.declination <= 43):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "january-july" + ", "
			
						i.save()




				elif (item.ascension+item.declination >= -4.93 and

					item.ascension+item.declination <= -4.92):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "march-july" + ", "
			
						i.save()



				elif (item.ascension+item.declination  >= 53 and 

				item.ascension+item.declination <=  54):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "february-july" + ", "
			
						i.save()


				elif (item.ascension+item.declination >=-9.2 and 
				item.ascension+item.declination <= -1.44):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "april-july" + ", "
			
						i.save()



				elif (item.ascension+item.declination >= 20.21 and 
				item.ascension+item.declination <= 20.22):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "june-october" + ", "
			
						i.save()



				elif (item.ascension+item.declination >= -8.18 and 
				item.ascension+item.declination <= -8.17):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "january-april" + ", "
			
						i.save()




				elif (item.ascension+item.declination >= 51.52 and

				item.ascension+item.declination <= 51.53):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "april-november" + ", "
			
						i.save()


				elif (item.ascension+item.declination >= 42.17 and 
				item.ascension+item.declination <= 42.18):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "april-october" + ", "
			
						i.save()


				elif (item.ascension+item.declination >= 31.71 and 
					item.ascension+item.declination <= 65.43):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "june-january" + ", "
			
						i.save()



				elif (item.ascension+item.declination >= 27.32 and 
				item.ascension+item.declination <= 30.46):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "september-march" + ", "
			
						i.save()



				elif (item.ascension+item.declination >= 60.78 and 
					item.ascension+item.declination <= 60.79):

					print(item.name)

					for i in qs:

						i.most_visible_periods += item.name + " : " + "december-august"+ ", "
			
						i.save()


			form = determine_most_visible_periods_Form()

	
	else:

		form = determine_most_visible_periods_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/determine-most-visible-periods.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })






def set_season(request):

	if request.method == 'POST':

		form = set_season_Form(request.POST)

		if form.is_valid():

			form.save()

			# obj = DaysInSearchEngine.objects.first()

			# qs = DaysInSearchEngine.objects.filter(id__gte=obj.id, id__lte=obj.id+93)

			
			obj = DaysInSearchEngine.objects.last()

			obj1 =  obj.first_id_set_season

			obj2 = obj.second_id_set_season

			qs = DaysInSearchEngine.objects.filter(id__gte=obj1, id__lte=obj2)


			for item in qs:

				item.season = " "

				if item.date_field.month == 12 or item.date_field.month == 1 or item.date_field.month == 2:

					item.season += "winter"

					item.save()

				elif item.date_field.month == 3 or item.date_field.month == 4 or item.date_field.month ==  5: 

					item.season += "spring"

					item.save()


				elif item.date_field.month == 6 or item.date_field.month == 7 or item.date_field.month == 8:

					item.season += "summer"

					item.save()

				elif item.date_field.month == 9 or item.date_field.month == 10 or item.date_field.month ==11 :

					item.season += "autumn"

					item.save()


			form = set_season_Form()

	
	else:

		form = set_season_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/set-season.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })








def determine_most_visible_periods_seasons(request):


	if request.method == 'POST':

		form = determine_most_visible_periods_seasons_Form(request.POST)

		if form.is_valid():

			form.save()

			print("strstr")

			# obj = DaysInSearchEngine.objects.first()

			# qs = DaysInSearchEngine.objects.filter(id__gte=obj.id, id__lte=obj.id+5)

			obj = DaysInSearchEngine.objects.last()

			obj1 =  obj.first_id_most_visible_periods_seasons

			obj2 = obj.second_id_most_visible_periods_seasons

			qs = DaysInSearchEngine.objects.filter(id__gte=obj1, id__lte=obj2)


			qs1 = Stars.objects.all()

			visl = []

			for i in qs:

				i.most_visible_periods_seasons = " "

			for item in qs1:

				# print("str")

				print(item.ascension+item.declination)

				if (item.ascension+item.declination  >= 59.06 and  

				item.ascension+item.declination <= 89.52):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()



				elif (item.ascension+item.declination  >= -9.97  and  

				item.ascension+item.declination <= -9.97):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()



				elif (item.ascension+item.declination  >= -46.17  and  

				item.ascension+item.declination <= -46.17):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -46.03  and  

				item.ascension+item.declination <= -46.03):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -46.1  and  

				item.ascension+item.declination <= -46.1):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()




				elif (item.ascension+item.declination  >= 12.57  and  

				item.ascension+item.declination <= 12.57):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -55.9  and  

				item.ascension+item.declination <= -55.9):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= 12.77  and  

				item.ascension+item.declination <= 12.77):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -50.29  and  

				item.ascension+item.declination <= -50.29):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -46.83  and  

				item.ascension+item.declination <= -46.83):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= -9.94  and  

				item.ascension+item.declination <= -9.94):

					print(item.name)

					for i in qs:

						i.most_visible_periods_seasons += item.name + ", "
			
						i.save()




				elif (item.ascension+item.declination  >= -1.29 and 
				 item.ascension+item.declination <= -0.07 ):

					print(item.name)

					for i in qs:

					

						if ( i.date_field.month == 10 or i.date_field.month ==11
						or i.date_field.month == 12 or i.date_field.month == 1 or i.date_field.month == 2):

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination  >= 20.49 and 

				item.ascension+item.declination <= 28.57):

					print(item.name)

					for i in qs:


						if (i.date_field.month ==11
						or i.date_field.month == 12 or i.date_field.month == 1 or i.date_field.month == 2

						or i.date_field.month == 3 or i.date_field.month == 4):


							i.most_visible_periods_seasons += item.name + ", " 
						
						i.save()



				elif (item.ascension+item.declination >= -6.39 and 

				item.ascension+item.declination <=  12.18):

					print(item.name)

					for i in qs:

						if (i.date_field.month == 5 or i.date_field.month == 6 
							or i.date_field.month == 7 or i.date_field.month == 8):


							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()



				elif (item.ascension+item.declination  >= -14.13 
				and item.ascension+item.declination <= -14.12):

					print(item.name)


					for i in qs:


						if (i.date_field.month == 2 or i.date_field.month == 3 or 
							i.date_field.month == 4 or i.date_field.month== 5):


							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()




				elif (item.ascension+item.declination  >= 20.38 and 
				item.ascension+item.declination <= 27.45):

					print(item.name)

					for i in qs:

						if (i.date_field.month == 8 or i.date_field.month == 9 or i.date_field.month == 10 or item.date_field ==11
						or i.date_field.month == 12 or i.date_field.month == 1 or i.date_field.month == 2):


							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()




				elif (item.ascension+item.declination >= 30.89 and 
				item.ascension+item.declination <= 41.05):

					print(item.name)

					for i in qs:

						if (i.date_field.month == 8 or i.date_field.month == 9 or i.date_field.month == 10 
							or i.date_field.month ==11
						or i.date_field.month == 12 or i.date_field.month == 1 or i.date_field.month == 2
						or i.date_field.month == 3 or i.date_field.month == 4):


							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()




				elif (item.ascension+item.declination >= 42 and 
				item.ascension+item.declination <= 43):

					print(item.name)

					for i in qs:

						if ( i.date_field.month == 1 or i.date_field.month == 2
						or i.date_field.month == 3 or i.date_field.month == 4 or i.date_field.month == 5
						or i.date_field.month == 6 or i.date_field.month == 7):

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()




				elif (item.ascension+item.declination >= -4.93 and

					item.ascension+item.declination <= -4.92):

					print(item.name)

					for i in qs:

						if (i.date_field.month == 3  or i.date_field.month == 4 or i.date_field.month == 5
						or i.date_field.month == 6 or i.date_field.month == 7 ):

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()



				elif (item.ascension+item.declination  >= 53 and 

				item.ascension+item.declination <=  54):

					print(item.name)

					for i in qs:


						if (i.date_field.month == 2 or i.date_field.month == 3
						or i.date_field.month == 4 or i.date_field.month== 5 or 
						i.date_field.month == 6 or i.date_field.month == 7):

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


				elif (item.ascension+item.declination >=-9.2 and 
				item.ascension+item.declination <= -1.44):

					print(item.name)

					for i in qs:


						if (i.date_field.month == 4 or i.date_field.month == 5 
							or i.date_field.month == 6 or i.date_field.month == 7):

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()



				elif (item.ascension+item.declination >= 20.21 and 
				item.ascension+item.declination <= 20.22):

					print(item.name)

					for i in qs:


						if ( i.date_field.month == 6 or i.date_field.month == 7 or 
						i.date_field.month == 8 or i.date_field.month == 9 
						or i.date_field.month == 10):

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()



				elif (item.ascension+item.declination >= -8.18 and 
				item.ascension+item.declination <= -8.17):

					print(item.name)

					for i in qs:

						if ( i.date_field.month == 1 or i.date_field.month == 2 
						or i.date_field.month == 3 or i.date_field.month == 4 ):
						

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()




				elif (item.ascension+item.declination >= 51.52 and

				item.ascension+item.declination <= 51.53):

					print(item.name)

					for i in qs:

						if (i.date_field.month == 4 or 
						i.date_field.month == 5 or i.date_field.month == 6
						or i.date_field.month == 7 or i.date_field.month == 8 
						or i.date_field.month == 9 or i.date_field.month == 10 
						or i.date_field.month == 11):

							i.most_visible_periods_seasons += item.name + ", "

						i.save()


				elif (item.ascension+item.declination >= 42.17 and 
				item.ascension+item.declination <= 42.18):

					print(item.name)

					for i in qs:

						if (i.date_field.month == 4 or 
						i.date_field.month == 5 or i.date_field.month == 6
						or i.date_field.month == 7 or i.date_field.month == 8 
						or i.date_field.month == 9 or i.date_field.month == 10
						or i.date_field.month == 11):

							 i.most_visible_periods_seasons += item.name + ", "

						i.save()


				elif (item.ascension+item.declination >= 31.71 and 
					item.ascension+item.declination <= 65.43):

					print(item.name)

					for i in qs:

						if ( i.date_field.month == 6
						or i.date_field.month == 7 or i.date_field.month == 8 
						or i.date_field.month == 9 or i.date_field.month == 10
						 or i.date_field.month == 11 or 
						i.date_field.month == 12 or i.date_field.month == 1):

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()



				elif (item.ascension+item.declination >= 27.32 and 
				item.ascension+item.declination <= 30.46):

					print(item.name)

					for i in qs:

						if (i.date_field.month == 9 or i.date_field.month == 10
						 or i.date_field.month == 11 or 
						i.date_field.month == 12 or i.date_field.month == 1
						or i.date_field.month == 2 or i.date_field.month == 3):

							i.most_visible_periods_seasons+= item.name + ", "
			
						i.save()



				elif (item.ascension+item.declination >= 60.78 and 
					item.ascension+item.declination <= 60.79):

					print(item.name)

					for i in qs:

						if (i.date_field.month == 12 or i.date_field.month == 1
						 or i.date_field.month == 2 or i.date_field.month == 3 
						 or i.date_field.month == 4 or i.date_field.month == 5
						  or i.date_field.month == 6 or i.date_field.month == 7 or 
						i.date_field.month == 8 ):
			

							i.most_visible_periods_seasons += item.name + ", "
			
						i.save()


			form = determine_most_visible_periods_seasons_Form()

	
	else:

		form = determine_most_visible_periods_seasons_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/determine-most-visible-periods.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })






def set_spring_equinox(request):


	if request.method == 'POST':

		form = set_spring_equinox_Form(request.POST)

		if form.is_valid():

			form.save()

			# obj = DaysInSearchEngine.objects.first()

			# qs = DaysInSearchEngine.objects.filter(id__gte=obj.id, id__lte=obj.id+93)

			obj = DaysInSearchEngine.objects.last()

			obj1 =  obj.first_id_set_spring_equinox

			obj2 = obj.second_id_set_spring_equinox

			qs = DaysInSearchEngine.objects.filter(id__gte=obj1, id__lte=obj2)


			for item in qs:

				i = item.date_field.year

				m = item.date_field.month

				j = item.date_field.day

				date_var = date(i, 12, 31) - date(i, 1, 1)

				date_var1 = date_var.days + 1


				if (date_var1 == 365 and  item.date_field.month == 3 and item.date_field.day  == 20):

					item.spring_equinox = True

					print("str")

					item.save()

				elif (date_var1  == 366  and item.date_field.month == 3 and item.date_field.day == 21):

					item.spring_equinox = True

					print("strstr")

					item.save()


			form = set_spring_equinox_Form()

	
	else:

		form = set_spring_equinox_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/set-spring-equinox.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })






def set_autumn_equinox(request):


	if request.method == 'POST':

		form = set_autumn_equinox_Form(request.POST)

		if form.is_valid():

			form.save()

			# obj = DaysInSearchEngine.objects.first()

			# qs = DaysInSearchEngine.objects.filter(id__gte=obj.id+183, id__lte=obj.id+366)

			obj = DaysInSearchEngine.objects.last()

			obj1 =  obj.first_id_set_autumn_equinox

			obj2 = obj.second_id_set_autumn_equinox

			qs = DaysInSearchEngine.objects.filter(id__gte=obj1, id__lte=obj2)


			for item in qs:

				i = item.date_field.year

				m = item.date_field.month

				j = item.date_field.day

				date_var = date(i, 12, 31) - date(i, 1, 1)

				date_var1 = date_var.days + 1


			
				if (date_var1 == 365 and  item.date_field.month == 9 and item.date_field.day  == 22):

					item.autumn_equinox = True

					print("str")

					item.save()

				elif (date_var1  == 366  and item.date_field.month == 9 and item.date_field.day == 23):

					item.autumn_equinox = True

					print("strstr")

					item.save()

			form = set_autumn_equinox_Form()

	
	else:

		form = set_autumn_equinox_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/set-autumn-equinox.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })






def set_summer_solstice(request):


	if request.method == 'POST':

		form = set_summer_solstice_Form(request.POST)

		if form.is_valid():

			form.save()

			# obj = DaysInSearchEngine.objects.first()

			# qs = DaysInSearchEngine.objects.filter(id__gte=obj.id, id__lte=obj.id+275)

			
			obj = DaysInSearchEngine.objects.last()

			obj1 =  obj.first_id_set_summer_solstice

			obj2 = obj.second_id_set_summer_solstice

			qs = DaysInSearchEngine.objects.filter(id__gte=obj1, id__lte=obj2)


			for item in qs:

				i = item.date_field.year

				m = item.date_field.month

				j = item.date_field.day

				date_var = date(i, 12, 31) - date(i, 1, 1)

				date_var1 = date_var.days + 1

			
				if (date_var1 == 365 and  item.date_field.month == 6 and item.date_field.day  == 20):

					item.summer_solstice= True

					print("str")

					item.save()

				elif (date_var1  == 366  and item.date_field.month == 6 and item.date_field.day == 21):

					item.summer_solstice = True

					print("strstr")

					item.save()

			form = set_summer_solstice_Form()

	
	else:

		form = set_summer_solstice_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/set-summer-solstice.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })






def set_winter_solstice(request):


	if request.method == 'POST':

		form = set_winter_solstice_Form(request.POST)

		if form.is_valid():

			form.save()

			# obj = DaysInSearchEngine.objects.first()

			# qs = DaysInSearchEngine.objects.filter(id__gte=obj.id+275, id__lte=obj.id+366)

			obj = DaysInSearchEngine.objects.last()

			obj1 =  obj.first_id_set_winter_solstice

			obj2 = obj.second_id_set_winter_solstice

			qs = DaysInSearchEngine.objects.filter(id__gte=obj1, id__lte=obj2)

			for item in qs:

				i = item.date_field.year

				m = item.date_field.month

				j = item.date_field.day

				date_var = date(i, 12, 31) - date(i, 1, 1)

				date_var1 = date_var.days + 1

			
				if (date_var1 == 365 and  item.date_field.month == 12 and item.date_field.day  == 21):

					item.winter_solstice= True

					print("str")

					item.save()

				elif (date_var1  == 366  and item.date_field.month == 12 and item.date_field.day == 22):

					item.winter_solstice = True

					print("strstr")

					item.save()

			form = set_winter_solstice_Form()

	
	else:

		form = set_winter_solstice_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/set-winter-solstice.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })







def determine_stars_movement(request):

	if request.method == 'POST':

		form = determine_stars_movement_Form(request.POST)

		if form.is_valid():

			form.save()


			obj = DaysInSearchEngine.objects.first()

			qs = DaysInSearchEngine.objects.filter(id__gte=obj.id, id__lte=obj.id+5)

			qs1 = Stars.objects.all()


			for item in qs1:

				if item.stars_temperature != 0 and item.stars_temperature < 5726:

					print(item.name)

					for i in qs:

						if item.name in i.most_visible_periods_seasons:

							i.stars_movement += ", " + item.name +  " less than 250km/s "

						i.save()

				elif item.stars_temperature != 0 and item.stars_temperature >= 5726:

					print(item.name)

					for i in qs:

						if item.name in i.most_visible_periods_seasons:

							i.stars_movement += ", " + item.name + " 250 km/s "


						i.save()

				

			form = determine_stars_movement_Form()

	
	else:

		form = determine_stars_movement_Form()

	if request.user.is_authenticated and request.user.is_staff:

		template_path = "Days/determine-stars-movement.html"

	else: 

		template_path = "Days/you-are-not-authorized-to-view-this-page.html"

	
	return render(request, template_path, {'form': form})# "obj":obj, })






def display_DaysInSearchEngine(request, id):

	obj = DaysInSearchEngine.objects.get(id=id)

	context = {'obj' : obj,}

	return render(request, "Days/display-DaysInSearchEngine.html", context)




























