
# coding: utf-8

# In[1]:
"""this script moves resting state, T2w, and ASL scan data for 
cross-sectional and longitudinal BABIES participants from
one directory structure to another, putting those scan data files 
in the target directory folders of the participants 
who have that data in the corresponding source directory folders. 
Importantly, this script only moves data from participants who have
resting state data - i.e., a file named 'rest.nii.gz', 'rest1.nii.gz', 
or 'rest2.nii.gz'. """

import re
import shutil
import os
import sys


# In[2]:


#get target directory names
target_dir = '/Users/franquerdasi/Box/subject_data/'
target_folders = []
for folder in sorted(next(os.walk(target_dir))[1]):
    folder_abs = os.path.abspath(os.path.join(target_dir, folder))
    target_folders = target_folders + [folder_abs]


def TargetToSource(folder_name):
    """this function takes a folder name from the target directory - 
    e.g., "0010-C-T1" and gives the corresponding folder name for that 
    participant and timepoint in the source directory, e.g., "010-C-T1"
    Input = target directory folder name 
    Outputs = source directory folder name
    """
    p = re.compile(r"[^-]*")
    m = p.findall(os.path.basename(folder_name))
    if m:
        if bool(re.search('[a-zA-Z]', m[0])):
            num_str = m[0][:-1]
        else:
            num_str = m[0]
            
        if int(num_str) < 1000:
            return os.path.basename(folder_name)[1:]
        else:
            return os.path.basename(folder_name)


#get equivalent source directory name as target directory
def SourceToTarget(folder_name):
    """this function takes a folder name from the source directory - 
    e.g., "010-C-T1" and gives the corresponding folder name for that 
    participant and timepoint in the target directory, e.g., "0010-C-T1"
    Input = source directory folder name 
    Outputs = target directory folder name
    """
    p = re.compile(r"[^-]*")
    m = p.findall(os.path.basename(folder_name))
    if m:
        if bool(re.search('[a-zA-Z]', m[0])):
            num_str = m[0][:-1]
        else:
            num_str = m[0]
        
        if int(num_str) < 1000:
            return "0" + os.path.basename(folder_name)
        else:
            return os.path.basename(folder_name)


# In[5]:


#get source directory names
source_dir = '/Volumes/group/active/BABIES/BABIES_6month/'
source_folders = []
for folder in sorted(next(os.walk(source_dir))[1]):
    folder_abs = os.path.abspath(os.path.join(source_dir, folder))
    source_folders = source_folders + [folder_abs]


# In[6]:


#copy rest.nii.gz files 
for folder in source_folders:
    folder_name = os.path.basename(folder)
    if os.path.exists(folder+'/rest.nii.gz'):
        if os.path.exists(target_dir+SourceToTarget(folder)) == False:
            new_dir = target_dir+SourceToTarget(folder)
            os.mkdir(new_dir)
            shutil.copyfile(folder+'/rest.nii.gz', new_dir+'/rest.nii.gz')
            print('new directory made for',folder_name,', rest.nii.gz copied')
        else:
            print('directory already exists for',folder_name)
            if os.path.exists(target_dir+SourceToTarget(folder)+'/rest.nii.gz'):
                print(folder_name,'already has rest')
            else:
                shutil.copyfile(folder+'/rest.nii.gz', target_dir+SourceToTarget(folder)+'/rest.nii.gz')
                print(folder_name,'rest.nii.gz copied')
    else:
        print(folder_name,'does not have rest')


# In[7]:


#copy rest1.nii.gz
for folder in source_folders:
    folder_name = os.path.basename(folder)
    if os.path.exists(folder+'/rest1.nii.gz'):
        if os.path.exists(target_dir+SourceToTarget(folder)) == False:
            new_dir = target_dir+SourceToTarget(folder)
            os.mkdir(new_dir)
            shutil.copyfile(folder+'/rest1.nii.gz', new_dir+'/rest1.nii.gz')
            print('new directory made for',folder_name,', rest1.nii.gz copied')
        else:
            print('directory already exists for',folder_name)
            #target_dir = source_dir+TargetToSource(folder)
            if os.path.exists(target_dir+SourceToTarget(folder)+'/rest1.nii.gz'):
                print(folder_name,'already has rest1')
            else:
                shutil.copyfile(folder+'/rest1.nii.gz', target_dir+SourceToTarget(folder)+'/rest1.nii.gz')
                print(folder_name,'rest1.nii.gz copied')
    else:
        print(folder_name,'does not have rest1')


# In[8]:


#copy rest2.nii.gz
for folder in source_folders:
    folder_name = os.path.basename(folder)
    if os.path.exists(folder+'/rest2.nii.gz'):
        if os.path.exists(target_dir+SourceToTarget(folder)) == False:
            new_dir = target_dir+SourceToTarget(folder)
            os.mkdir(new_dir)
            shutil.copyfile(folder+'/rest2.nii.gz', new_dir+'/rest2.nii.gz')
            print('new directory made for',folder_name,', rest2.nii.gz copied')
        else:
            print('directory already exists for',folder_name)
            #target_dir = source_dir+TargetToSource(folder)
            if os.path.exists(target_dir+SourceToTarget(folder)+'/rest2.nii.gz'):
                print(folder_name,'already has rest2')
            else:
                shutil.copyfile(folder+'/rest2.nii.gz', target_dir+SourceToTarget(folder)+'/rest2.nii.gz')
                print(folder_name,'rest2.nii.gz copied')
    else:
        print(folder_name,'does not have rest2')


# In[9]:


#copy t2w.nii.gz
for t_folder in target_folders:
    t_folder_name = os.path.basename(t_folder)
    if os.path.exists(t_folder):
        if os.path.exists(source_dir+TargetToSource(t_folder)+'/t2w_0_8mm_sag.nii.gz'):
            dest_folder = source_dir+TargetToSource(t_folder)
            shutil.copyfile(dest_folder+'/t2w_0_8mm_sag.nii.gz', t_folder+'/t2w_0_8mm_sag.nii.gz')
            print(t_folder_name,'t2w copied')
        else:
            print(t_folder_name,'does not have t2w')


# In[10]:


#copy asl.nii.gz
for t_folder in target_folders:
    t_folder_name = os.path.basename(t_folder)
    if os.path.exists(t_folder):
        if os.path.exists(source_dir+TargetToSource(t_folder)+'/asl.nii.gz'):
            dest_folder = source_dir+TargetToSource(t_folder)
            shutil.copyfile(dest_folder+'/asl.nii.gz', t_folder+'/asl.nii.gz')
            print(t_folder_name,'asl copied')
        else:
            print(t_folder_name,'does not have asl')

