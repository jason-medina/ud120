# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:48:25 2017

@author: JasonMedina
"""

list1 = ['poi', 'salary', 'total_stock_value', 'expenses', 'bonus',
          'exercised_stock_options', 'deferred_income',
          'to_poi_fraction', 'from_poi_to_this_person', 'from_poi_fraction',
          'shared_receipt_with_poi']

list2 = ['poi',
 'bonus',
 'salary',
 'deferral_payments',
 'deferred_income',
 'director_fees',
 'exercised_stock_options',
 'expenses',
 'total_payments',
 'total_stock_value',
 'from_messages',
 'from_poi_to_this_person',
 'from_this_person_to_poi',
 'loan_advances',
 'long_term_incentive',
 'other',
 'restricted_stock',
 'restricted_stock_deferred',
 'salary',
 'shared_receipt_with_poi',
 'to_messages']
 
 set([list1]) - set([list2])
