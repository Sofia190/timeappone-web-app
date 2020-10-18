"""TIMEAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from .views_1st import welcome

from Searches.views import search_view

from Days.views import (view_days_till_a_date, view_days_till_a_date_display_attributes,

view_years_with_equal_sum_of_attributes_to_a_value, view_leap_years_in_a_decade, 

view_leap_years_in_a_century, view_sum_of_attributes_of_nth_day_in_a_year,

view_how_many_bisect_years_in_the_last_nth_centuries,

how_many_months_and_days_till_the_next_spring_equinox,

how_many_months_and_days_till_the_next_autumn_equinox,

what_period_between_years_with_total_lunar_eclipse,

find_the_equivalent_of_timezone_with_USA,

find_the_difference_of_timezone_with_USA,

display_calculators_page_view,

find_equivalent_with_timezone,

find_difference_with_timezone,

find_difference_of_timezone_from_UTC,

find_difference_between_two_timezones,

display_date_for_the_next_n_days,

find_dates_with_attributes_of_time_equal_to_date_in_a_decade,

find_dates_with_attributes_of_time_equal_to_date_in_a_century,

find_time_until_a_date_after_n_years,

calculate_date_and_time_until_next_solstice,

calculate_date_and_time_until_the_nth_day_in_the_next_n_years,

find_which_years_of_nth_century_have_more_than_n_days_with_attrs,)



urlpatterns = [
    path('admin/', admin.site.urls),

    path('start-page/', welcome, name="welcome"),

    path('search/', search_view),

    path('days/', view_days_till_a_date, name="view_days_till_a_date"),

    path('days-display-attributes/', view_days_till_a_date_display_attributes, name="view_days_till_a_date_display_attributes"),

    path('attributes-equal-to-a-value/', view_years_with_equal_sum_of_attributes_to_a_value, name="view_years_with_equal_sum_of_attributes_to_a_value"),

    path('leap-years-in-a-decade/', view_leap_years_in_a_decade, name="view_leap_years_in_a_decade"),

    path('leap-years-in-a-century/', view_leap_years_in_a_century, name="view_leap_years_in_a_century"),

    path('sum-of-attributes/', view_sum_of_attributes_of_nth_day_in_a_year, name="view_sum_of_attributes_of_nth_day_in_a_year"),

    path('bisect-years-in-centuries/',  view_how_many_bisect_years_in_the_last_nth_centuries
, name="view_how_many_bisect_years_in_the_last_nth_centuries"),

    path('next-spring-equinox-periods/', how_many_months_and_days_till_the_next_spring_equinox,
    name="how_many_months_and_days_till_the_next_spring_equinox"),


    path('next-autumn-equinox-periods/', how_many_months_and_days_till_the_next_autumn_equinox,
    name="how_many_months_and_days_till_the_next_autumn_equinox"),

    path('lunar-eclipse-dates-periods/', what_period_between_years_with_total_lunar_eclipse, name="what_period_between_years_with_total_lunar_eclipse"),

    path('equivalent-of-timezone-with-USA/', find_the_equivalent_of_timezone_with_USA, name="find_the_equivalent_of_timezone_with_USA"),

    path('difference-of-timezone-with-USA/', find_the_difference_of_timezone_with_USA, name="find_the_difference_of_timezone_with_USA"),

    path('time-and-date-calculators/', display_calculators_page_view, name="display_calculators_page_view"),

    path('equivalent-with-timezone/', find_equivalent_with_timezone, name="find_equivalent_with_timezone"),

    path('difference-with-timezone/', find_difference_with_timezone, name='find_difference_with_timezone'),
    
    path('difference-of-timezone-from-UTC/',  find_difference_of_timezone_from_UTC, name="find_difference_of_timezone_from_UTC"),  

    path('difference-between-two-timezones/', find_difference_between_two_timezones, name="find_difference_between_two_timezones"),

    path('start-page/time-and-date-calculators/', display_calculators_page_view, name="display_calculators_page_view"),

    path('date-for-the-next-n-days/', display_date_for_the_next_n_days, name='display_date_for_the_next_n_days'),

    path('attributes-of-time-equal-to-date-in-a-decade', find_dates_with_attributes_of_time_equal_to_date_in_a_decade,

        name='find_dates_with_attributes_of_time_equal_to_date_in_a_decade'),

    path('attributes-of-time-equal-to-date-in-a-century/', find_dates_with_attributes_of_time_equal_to_date_in_a_century,

        name='find_dates_with_attributes_of_time_equal_to_date_in_a_century'),


    path('time-until-a-date-after-n-years/', find_time_until_a_date_after_n_years, name="find_time_until_a_date_after_n_years"),

    path('date-and-time-until-next-solstice/', calculate_date_and_time_until_next_solstice, 

        name='calculate_date_and_time_until_next_solstice'),

    path('date-and-time-until-the-nth-day-in-the-next-n-years/', calculate_date_and_time_until_the_nth_day_in_the_next_n_years,

        name="calculate_date_and_time_until_the_nth_day_in_the_next_n_years"),

    path('years-of-nth-century-have-more-than-n-days-with-attrs/', find_which_years_of_nth_century_have_more_than_n_days_with_attrs,

        name="find_which_years_of_nth_century_have_more_than_n_days_with_attrs"),



]












