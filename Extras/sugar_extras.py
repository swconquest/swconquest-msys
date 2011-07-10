import string

from header_operations import *

#===============================================================================
# Troop wrapper
#===============================================================================
class T:
	def __init__(self, ID):
		if (ID[0] == ":") or (ID[0] == "$"):
			self.ID = ID
		else: 
			self.ID = "trp_" + ID 

	def has_item_equipped(self, item, modifier=0):
		return (modifier | troop_has_item_equipped, self.ID, item)
	
	def is_mounted(self, modifier=0):               
		return (modifier | troop_is_mounted, self.ID)
	
	def is_guarantee_ranged(self, modifier=0):               
		return (modifier | troop_is_guarantee_ranged, self.ID)
	
	def is_guarantee_horse(self, modifier=0):               
		return(modifier | troop_is_guarantee_horse, self.ID)
	
	def set_name(self,string_no):               
		return(troop_set_name, self.ID, string_no)
	
	def set_plural_name  (self, string_no):
		return (troop_set_plural_name, self.ID, string_no)
	
	def set_face_key_from_current_profile (self):
		return (troop_set_face_key_from_current_profile, self.ID)
	
	def set_type(self,gender):
		return (troop_set_type,self.ID,gender)
	
	def get_type(self,destination):
		return(troop_get_type,destination,self.ID)
	
	def is_hero(self):
		return(troop_is_hero,self.ID)
	
	def is_wounded(self):
		return(troop_is_wounded,self.ID)
	
	def set_auto_equip(self,value):  
		return(troop_set_auto_equip,self.ID,value)
	
	def ensure_inventory_space(self,value):
		return(troop_ensure_inventory_space,self.ID,value)
	
	def sort_inventory(self):
		return(troop_sort_inventory,self.ID)
	
	def add_merchandise(self,item,quantity):
		return(troop_add_merchandise,self.ID,quantity)
	
	def add_merchandise_with_faction(self,faction,item,quantity):     
		return(troop_add_merchandise_with_faction,self.ID,faction,item,quantity)
	
	def get_xp(self,destination):
		return(troop_get_xp, destination, self.ID)
	
	def get_class(self,destination):
		return(troop_get_class, destination, self.ID)
	
	def set_class(self,value):                        
		return(troop_set_class, self.ID, value)

	def raise_attribute(self,attribute,value):
		return(troop_raise_attribute,self.ID,attribute,value)
	
	def raise_skill(self,skill,value):
		return(troop_raise_skill,self.ID,skill,value)
	
	def raise_proficiency(self,proficiency,value):
		return(troop_raise_proficiency,self.ID,proficiency,value)
	
	def raise_proficiency_linear (self,proficiency,value):
		return(troop_raise_proficiency,self.ID,proficiency,value)

	def add_proficiency_points(self,value):
		return(troop_add_proficiency_points,self.id,value)		
				
	def add_gold  (self, value):
		return(troop_add_gold, self.id, value)
	
	def remove_gold  (self, value):
		return(troop_remove_gold, self.id, value)
	
	def add_item   (self, item, modifier= -1):
		if modifier == -1: 
			return(troop_add_item, self.id, item)
		else :
			return(troop_add_item, self.id, item, modifier)
		
	def remove_item  (self, item):
		return(troop_remove_item,self.id,item)
	
	def clear_inventory(self):  
		return(troop_clear_inventory,self.id)
	
	def equip_items(self):
		return(troop_equip_items,self.id)
	
	def inventory_slot_set_item_amount(self,inventory_slot_no,value):  
		return(troop_inventory_slot_set_item_amount,self.id,inventory_slot_no,value)
	
	def inventory_slot_get_item_amount(self,destination,inventory_slot_no):  
		return(troop_inventory_slot_get_item_amount,destination,self.id,inventory_slot_no)
	
	def inventory_slot_get_item_max_amount(self, destination, inventory_slot_no):
		return(troop_inventory_slot_get_item_max_amount, destination, self.id, inventory_slot_no)

	def add_items(self, item, number):                       
		return(troop_add_items, self.id, item, number)

	def remove_items(self, item, number):        
		return(troop_remove_items, self.id, item, number)

	def loot_troop (self, target_troop, probability):                      
		return(troop_loot_troop, target_troop, self.id, probability) 

	def get_inventory_capacity(self,destination):           
		return(troop_get_inventory_capacity,destination,self.id)
	
	def get_inventory_slot(self,destination,inventory_slot_no):              
		return(troop_get_inventory_slot,destination,self.id,inventory_slot_no)
	
	def get_inventory_slot_modifier  (self,destination,inventory_slot_no):    
		return(troop_get_inventory_slot_modifier,destination,self.id,inventory_slot_no)
	
	def set_inventory_slot (self,inventory_slot_no,value):            
		return(troop_set_inventory_slot,self.id,inventory_slot_no,value)
	
	def set_inventory_slot_modifier (self,inventory_slot_no,value):    
		return(troop_set_inventory_slot_modifier,self.id,inventory_slot_no,value)
	
	def set_faction(self,faction):                     
		return(troop_set_faction,self.id,faction)
	
	def set_age(self,age_slider_pos):                         
		return(troop_set_age, self.id, age_slider_pos) 
	
	def set_health(self,relative_health):                      
		return(troop_set_health,self.id,relative_health)

	def get_upgrade_troop (self,destination,upgrade_path ):               
		return(troop_get_upgrade_troop,destination,self.id,upgrade_path) 

	def set_slot(self, slot_no, value):              
		return(troop_set_slot, self.id, slot_no, value)

	def get_slot (self, destination, slot_no):                  
		return(troop_get_slot, destination, self.id, slot_no)


#===============================================================================
# Quest wrapper
#===============================================================================
class Q:
	def __init__(self, ID):
		if (ID[0] == ":") or (ID[0] == "$"):
			self.ID = ID
		else: 
			self.ID = "qst_" + ID
	
	def is_active (self, modifier=0):               
		return (modifier | check_quest_active, self.ID)
	
	def is_finished(self, modifier=0):               
		return (modifier | check_quest_finished, self.ID)
	
	def is_succeeded(self, modifier=0):               
		return (modifier | check_quest_succeeded, self.ID)
	
	def is_failed(self, modifier=0):               
		return (modifier | check_quest_failed, self.ID)
	
	def is_concluded (self, modifier=0):               
		return (modifier | check_quest_concluded, self.ID)
		
		
		
## Swyter Version

import string

from header_operations import *

#===============================================================================
# Troop wrapper
#===============================================================================
class troop:
	def __init__(self, ID):
		if (ID[0] == ":") or (ID[0] == "$"):
			self.ID = ID
		else: 
			self.ID = "trp_" + ID 

	def has_item_equipped(self, item, modifier=0):
		return (modifier | troop_has_item_equipped, self.ID, item)
	
	def is_mounted(self, modifier=0):               
		return (modifier | troop_is_mounted, self.ID)
	
	def is_guarantee_ranged(self, modifier=0):               
		return (modifier | troop_is_guarantee_ranged, self.ID)
	
	def is_guarantee_horse(self, modifier=0):               
		return(modifier | troop_is_guarantee_horse, self.ID)
	
	def set_name(self,string_no):               
		return(troop_set_name, self.ID, string_no)
	
	def set_plural_name  (self, string_no):
		return (troop_set_plural_name, self.ID, string_no)
	
	def set_face_key_from_current_profile (self):
		return (troop_set_face_key_from_current_profile, self.ID)
	
	def set_type(self,gender):
		return (troop_set_type,self.ID,gender)
	
	def get_type(self,destination):
		return(troop_get_type,destination,self.ID)
	
	def is_hero(self):
		return(troop_is_hero,self.ID)
	
	def is_wounded(self):
		return(troop_is_wounded,self.ID)
	
	def set_auto_equip(self,value):  
		return(troop_set_auto_equip,self.ID,value)
	
	def ensure_inventory_space(self,value):
		return(troop_ensure_inventory_space,self.ID,value)
	
	def sort_inventory(self):
		return(troop_sort_inventory,self.ID)
	
	def add_merchandise(self,item,quantity):
		return(troop_add_merchandise,self.ID,quantity)
	
	def add_merchandise_with_faction(self,faction,item,quantity):     
		return(troop_add_merchandise_with_faction,self.ID,faction,item,quantity)
	
	def get_xp(self,destination):
		return(troop_get_xp, destination, self.ID)
	
	def get_class(self,destination):
		return(troop_get_class, destination, self.ID)
	
	def set_class(self,value):                        
		return(troop_set_class, self.ID, value)

	def raise_attribute(self,attribute,value):
		return(troop_raise_attribute,self.ID,attribute,value)
	
	def raise_skill(self,skill,value):
		return(troop_raise_skill,self.ID,skill,value)
	
	def raise_proficiency(self,proficiency,value):
		return(troop_raise_proficiency,self.ID,proficiency,value)
	
	def raise_proficiency_linear (self,proficiency,value):
		return(troop_raise_proficiency,self.ID,proficiency,value)

	def add_proficiency_points(self,value):
		return(troop_add_proficiency_points,self.id,value)		
				
	def add_gold  (self, value):
		return(troop_add_gold, self.id, value)
	
	def remove_gold  (self, value):
		return(troop_remove_gold, self.id, value)
	
	def add_item   (self, item, modifier= -1):
		if modifier == -1: 
			return(troop_add_item, self.id, item)
		else :
			return(troop_add_item, self.id, item, modifier)
		
	def remove_item  (self, item):
		return(troop_remove_item,self.id,item)
	
	def clear_inventory(self):  
		return(troop_clear_inventory,self.id)
	
	def equip_items(self):
		return(troop_equip_items,self.id)
	
	def inventory_slot_set_item_amount(self,inventory_slot_no,value):  
		return(troop_inventory_slot_set_item_amount,self.id,inventory_slot_no,value)
	
	def inventory_slot_get_item_amount(self,destination,inventory_slot_no):  
		return(troop_inventory_slot_get_item_amount,destination,self.id,inventory_slot_no)
	
	def inventory_slot_get_item_max_amount(self, destination, inventory_slot_no):
		return(troop_inventory_slot_get_item_max_amount, destination, self.id, inventory_slot_no)

	def add_items(self, item, number):                       
		return(troop_add_items, self.id, item, number)

	def remove_items(self, item, number):        
		return(troop_remove_items, self.id, item, number)

	def loot_troop (self, target_troop, probability):                      
		return(troop_loot_troop, target_troop, self.id, probability) 

	def get_inventory_capacity(self,destination):           
		return(troop_get_inventory_capacity,destination,self.id)
	
	def get_inventory_slot(self,destination,inventory_slot_no):              
		return(troop_get_inventory_slot,destination,self.id,inventory_slot_no)
	
	def get_inventory_slot_modifier  (self,destination,inventory_slot_no):    
		return(troop_get_inventory_slot_modifier,destination,self.id,inventory_slot_no)
	
	def set_inventory_slot (self,inventory_slot_no,value):            
		return(troop_set_inventory_slot,self.id,inventory_slot_no,value)
	
	def set_inventory_slot_modifier (self,inventory_slot_no,value):    
		return(troop_set_inventory_slot_modifier,self.id,inventory_slot_no,value)
	
	def set_faction(self,faction):                     
		return(troop_set_faction,self.id,faction)
	
	def set_age(self,age_slider_pos):                         
		return(troop_set_age, self.id, age_slider_pos) 
	
	def set_health(self,relative_health):                      
		return(troop_set_health,self.id,relative_health)

	def get_upgrade_troop (self,destination,upgrade_path ):               
		return(troop_get_upgrade_troop,destination,self.id,upgrade_path) 

	def set_slot(self, slot_no, value):              
		return(troop_set_slot, self.id, slot_no, value)

	def get_slot (self, destination, slot_no):                  
		return(troop_get_slot, destination, self.id, slot_no)


#===============================================================================
# Quest wrapper
#===============================================================================
class quest:
	def __init__(self, ID):
		if (ID[0] == ":") or (ID[0] == "$"):
			self.ID = ID
		else: 
			self.ID = "qst_" + ID
	
	def is_active (self, modifier=0):               
		return (modifier | check_quest_active, self.ID)
	
	def is_finished(self, modifier=0):               
		return (modifier | check_quest_finished, self.ID)
	
	def is_succeeded(self, modifier=0):               
		return (modifier | check_quest_succeeded, self.ID)
	
	def is_failed(self, modifier=0):               
		return (modifier | check_quest_failed, self.ID)
	
	def is_concluded (self, modifier=0):               
		return (modifier | check_quest_concluded, self.ID)




