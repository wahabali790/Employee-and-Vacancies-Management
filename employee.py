#!/usr/bin/env python
# coding: utf-8

# # Read Employee.json

# In[1]:


import json
with open('Downloads/employees.json') as f:
    emp=json.load(f)
    print(emp)


# # Read Vaccancies.json

# In[2]:


import json
with open('Downloads/Vacancies 3.json') as f:
    vac=json.load(f)
    print(vac)


# # Soft skills

# In[3]:


d_soft = {}
for employee in emp:
    empl=employee['Soft Skills']
    for vacancies in vac:
        vaccan=vacancies['Soft Skills'].split(',')
            
        match=set(empl) & set(vaccan)
        per_soft=(len(match)/len(vaccan))*100
        employee_name = employee['Name']
        vacancy_id = vacancies['ID']
        if employee_name not in d_soft:
            d_soft[employee_name] = {}
        d_soft[employee_name][vacancy_id] = per_soft
print(d_soft) 


# # Hard Skills

# In[4]:


d_hard={}
for employee in emp:
    
    empl=employee['Hard Skills']
        
    for vacan in vac:
        vacancies=vacan['Hard Skills'].split(',')
            
        match=set(empl) & set(vacancies)
        perc_hard=(len(match)/len(vacancies))*100#percentage of matched values
        employee_name = employee['Name']
        vacancy_id = vacan['ID']
        if employee_name not in d_hard:
            d_hard[employee_name] = {}
        d_hard[employee_name][vacancy_id] = perc_hard
print(d_hard)
        


# # salary 

# In[22]:


d_salary={}
for employee in emp:
    empl=employee['Salary Aim']
    
    
    for vacancies in vac:
        vaccan=vacancies['Salary']
        match=0
        
        if empl<=vaccan:
            match+=1
        else:
            match=0
        employee_name = employee['Name']
        vacancy_id = vacancies['ID']
        if employee_name not in d_salary:
            d_salary[employee_name] = {}
        d_salary[employee_name][vacancy_id] = match

print(d_salary)


# # Location

# In[6]:


d_location={}
for employee in emp:
    
    
    e_coun=employee['Location']['Country']
    e_city=employee['Location']['City']
    
    for vacancies in vac:
        v_coun=vacancies['Country']
        v_city=vacancies['City']
        
        match=0
        if e_coun==v_coun:
            match+=1
            if e_city==v_city:
                match+=1
        elif e_coun==v_coun and e_city!=v_city:
            match+=1
        else:
            match=0
            
        employee_name = employee['Name']
        vacancy_id = vacancies['ID']
        
        if employee_name not in d_location:
            d_location[employee_name] = {}
        d_location[employee_name][vacancy_id] = match
            
            
        
print(d_location)


# # Experience

# In[7]:


d_exp={}
for employee in emp:
    empl=employee['Years of experience']
    
    for vacancies in vac:
        vaccan=vacancies['Experience']
        
        match=0
        if empl>=vaccan:
            match+=1
        else:
            match=0
            
        employee_name = employee['Name']
        vacancy_id = vacancies['ID']
        
        if employee_name not in d_exp:
            d_exp[employee_name] = {}
        d_exp[employee_name][vacancy_id] = match
print(d_exp)


# In[18]:


Average = {}
for name in d_soft:
    Average[name] = {}
    for key in d_soft[name]:
        Average[name][key] = (d_soft[name][key] + d_hard[name][key]+d_salary[name][key]+d_location[name][key]+d_exp[name][key])/5


# In[20]:


print(Average)


# # test code

# In[14]:


d_soft = {}
for employee in emp:
    empl=employee['Soft Skills']
    for vacancies in vac:
        vaccan=vacancies['Soft Skills'].split(',')
            #print(vaccan)
            #print(set(empl) & set(vaccan))#it will print the matched values in a set
        match=set(empl) & set(vaccan)
        per_soft=(len(match)/len(vaccan))*100
        employee_name = employee['Name']
        vacancy_id = vacancies['ID']
        if employee_name not in d_soft:
            d_soft[employee_name] = {}
        d_soft[employee_name][vacancy_id] = per_soft
        
        
        
print(d_soft)       


# In[15]:


d_hard={}
for employee in emp:
    
    empl=employee['Hard Skills']
        #print([employee["Name"]],':')
        #print(empl)
    for vacan in vac:
        vacancies=vacan['Hard Skills'].split(',')
            
        match=set(empl) & set(vacancies)
        perc_hard=(len(match)/len(vacancies))*100#percentage of matched values
        employee_name = employee['Name']
        vacancy_id = vacan['ID']
        if employee_name not in d_hard:
            d_hard[employee_name] = {}
        d_hard[employee_name][vacancy_id] = perc_hard
print(d_hard)


# In[16]:


d_salary={}
for employee in emp:
    empl=employee['Salary Aim']
    
    for vacancies in vac:
        vaccan=vacancies['Salary']
        match=0
        
        if empl<=vaccan:
            
            match+=1
        else:
            match=0
        employee_name = employee['Name']
        vacancy_id = vacancies['ID']
        if employee_name not in d_salary:
            d_salary[employee_name] = {}
        d_salary[employee_name][vacancy_id] = match
print(d_salary)


# In[17]:


d_exp={}
for employee in emp:
    empl=employee['Years of experience']
    
    
    
    for vacancies in vac:
        vaccan=vacancies['Experience']
        
        match=0
        if empl>=vaccan:
            match+=1
        else:
            match=0
        employee_name = employee['Name']
        vacancy_id = vacancies['ID']
        if employee_name not in d_exp:
            d_exp[employee_name] = {}
        d_exp[employee_name][vacancy_id] = match
print(d_exp)


# In[18]:


d_location={}
for employee in emp:
    
    
    e_coun=employee['Location']['Country']
    e_city=employee['Location']['City']
    
    
    
    
    for vacancies in vac:
        v_coun=vacancies['Country']
        v_city=vacancies['City']
        
        match=0
        if e_coun==v_coun:
            match+=1
            if e_city==v_city:
                match+=1
        elif e_coun==v_coun and e_city!=v_city:
            match+=1
        else:
            
            match=0
        employee_name = employee['Name']
        vacancy_id = vacancies['ID']
        if employee_name not in d_location:
            d_location[employee_name] = {}
        d_location[employee_name][vacancy_id] = match
            
            
        
print(d_location)


# In[ ]:





# In[19]:


result


# In[ ]:





# In[20]:


soft = {'Jima Perez': {1: 20.0, 2: 33.33333333333333, 3: 0.0, 4: 33.33333333333333, 5: 33.33333333333333, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 33.33333333333333}}
hard = {'Jima Perez': {1: 0.0, 2: 20.0, 3: 20.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 20.0, 8: 0.0, 9: 0.0, 10: 0.0}}

result = {}
for name in soft:
    result[name] = {}
    for key in soft[name]:
        result[name][key] = soft[name][key] + hard[name][key]

print(result)


# In[21]:


# Define a nested dictionary with empty lists
my_dict = {
    'level1': {
        'level2a': [],
        'level2b': []
    },
    'level1b': {
        'level2c': []
    }
}

# Nested loop to iterate over some data
for i in range(3):
    for j in range(2):
        if i == 0:
            my_dict['level1']['level2a'].append(j)
        elif i == 1:
            my_dict['level1']['level2b'].append(j)
        else:
            my_dict['level1b']['level2c'].append(j)

print(my_dict)


# In[22]:


w={'w':{1:'e'}}
w['w'][1]='r'


# In[23]:


w


# In[24]:


w={'wahab':'1'}


# In[ ]:


d_hard={}
for employee in emp:
    
    empl=employee['Hard Skills']
        
    for vacan in vac:
        vacancies=vacan['Hard Skills'].split(',')
            
        match=set(empl) & set(vacancies)
        perc_hard=(len(match)/len(vacancies))*100#percentage of matched values
        
        if employee['Name'] not in d_hard:
            d_hard[employee['Name']] = {}
        d_hard[employee['Name']][vacan['ID']] = perc_hard
print(d_hard)


# In[ ]:


result = {}
for name in d_soft:
    result[name] = {}
    for key in d_soft[name]:
        result[name][key] = (d_soft[name][key] + d_hard[name][key])/2


# In[ ]:




