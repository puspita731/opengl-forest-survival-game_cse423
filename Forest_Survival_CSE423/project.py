def draw_gun1():
   
    glPushMatrix()
    glColor3f(0.2, 0.2, 0.2)
    glScalef(1.0, 0.3, 0.3)
    glutSolidCube(10)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.7, 0.7, 0.7)
    glTranslatef(5, 0, 0)
    glScalef(0.5, 0.2, 0.2)
    glutSolidCube(10)
    glPopMatrix()

def draw_gun2():
    
    glPushMatrix()
    glColor3f(0.1, 0.1, 0.1)
    glScalef(0.6, 0.2, 0.2)
    glutSolidCube(8)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.8, 0.6, 0.2)
    glTranslatef(2.5, 0, -1)
    glScalef(0.2, 0.15, 0.4)
    glutSolidCube(8)
    glPopMatrix()

class Player:
    def __init__(self, pos=(0,0,0)):
        self.pos = pos

    def draw(self):
        global is_walking, walking_animation_time
        x, y, z = self.pos
        glPushMatrix()
        glTranslatef(x, y, z)
        
        
        submerge_offset = 0
        if in_water:
            
            _, water_depth = check_water_collision(x, y)
           
            submerge_offset = -(water_depth * 0.8)  
            glTranslatef(0, 0, submerge_offset)
        

        glScalef(1.25, 1.25, 1.25)
        
        
        glPushMatrix()
        glTranslatef(-2.5, 0, 0)  
        
        
        left_leg_swing = 0
        left_knee_bend = 0
        if is_walking:
            
            left_leg_swing = 80.0 * math.sin(walking_animation_time)  
            left_knee_bend = 55.0 * abs(math.sin(walking_animation_time * 2))  
        
       
        glRotatef(left_leg_swing, 1, 0, 0)  
        glColor3f(0.2, 0.2, 0.7)  
        
        
        glPushMatrix()
        glTranslatef(0, 0, 6.0)   
        glScalef(2.0, 2.0, 6.0)   
        glutSolidCube(1.0)
        glPopMatrix()
        
        
        glPushMatrix()
        glTranslatef(0, 0, 3.0)   
        glRotatef(-left_knee_bend, 1, 0, 0)  
        glTranslatef(0, 0, -2.0)   
        glScalef(1.7, 1.7, 4.0)   
        glutSolidCube(1.0)
        glPopMatrix()
        
        
        glPushMatrix()
        
        foot_lift = 0
        if is_walking:
            
            foot_lift = max(0, 4.0 * math.sin(walking_animation_time)) 
        
        glTranslatef(0, -1.5, -2.0 + foot_lift) 
        glColor3f(0.1, 0.1, 0.1)   
        glScalef(2.2, 3.5, 1.2)   
        glutSolidCube(1.0)
        glPopMatrix()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(2.5, 0, 0)   
        
       
        right_leg_swing = 0
        right_knee_bend = 0
        if is_walking:
           
            right_leg_swing = -60.0 * math.sin(walking_animation_time)
            right_knee_bend = 35.0 * abs(math.sin(walking_animation_time * 2 + math.pi))  
        
      
        glRotatef(right_leg_swing, 1, 0, 0)  
        glColor3f(0.2, 0.2, 0.7) 
        
     
        glPushMatrix()
        glTranslatef(0, 0, 6.0)   
        glScalef(2.0, 2.0, 6.0)   
        glutSolidCube(1.0)
        glPopMatrix()
        
        
        glPushMatrix()
        glTranslatef(0, 0, 3.0)   
        glRotatef(-right_knee_bend, 1, 0, 0) 
        glTranslatef(0, 0, -2.0) 
        glScalef(1.7, 1.7, 4.0)   
        glutSolidCube(1.0)
        glPopMatrix()
        
        
        glPushMatrix()
        
        foot_lift = 0
        if is_walking:
            
            foot_lift = max(0, 4.0 * math.sin(walking_animation_time + math.pi)) 
        
        glTranslatef(0, -1.5, -2.0 + foot_lift)  
        glColor3f(0.1, 0.1, 0.1)  
        glScalef(2.2, 3.5, 1.2)    
        glutSolidCube(1.0)
        glPopMatrix()
        glPopMatrix()
       
        # Draw body - with super power visual effects
        glPushMatrix()
        glTranslatef(0, 0, 12)
        
        # Add super power visual effects
        global cheat_mode_active
        if cheat_mode_active:
            # Make player glow with bright colors when super power is active
            glow_intensity = 0.5 + 0.5 * math.sin(time.time() * 10)  # Pulsing effect
            glColor3f(1.0, 1.0 - glow_intensity * 0.5, 0.2 + glow_intensity * 0.3)  # Bright golden glow
            glScalef(1.1, 0.9, 1.3)  # Slightly larger and taller when powered up
        else:
            glColor3f(0.8, 0.5, 0.2)  # Normal skin color
            glScalef(1.0, 0.8, 1.2)  # Normal size
        
        glutSolidCube(8)
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(0, 0, 20)
        glColor3f(1.0, 0.85, 0.7)
        glutSolidSphere(3, 16, 12)
        glPopMatrix()
       
        glPushMatrix()
        glTranslatef(0, 0, 22)
        glColor3f(0.4, 0.2, 0.1)  
        glutSolidSphere(3.5, 12, 8)
        glPopMatrix()
        
       
        global camera_yaw
        yaw_deg = camera_yaw
        
       
        glPushMatrix()
        glTranslatef(-3.5, 0.0, 18)  
        glRotatef(yaw_deg + 15, 0, 0, 1) 
        glRotatef(-10, 1, 0, 0)     
        glRotatef(5, 0, 1, 0)      
        glColor3f(1.0, 0.85, 0.7) 
        
        glPushMatrix()
        glTranslatef(0, 3.0, 0)
        glScalef(1.8, 6.0, 1.8)    
        glutSolidCube(1.0)
        glPopMatrix()
        
       
        glPushMatrix()
        glTranslatef(0, 8.0, 0)
        glScalef(1.5, 5.0, 1.5)    
        glutSolidCube(1.0)
        glPopMatrix()
        
       
        glPushMatrix()
        glTranslatef(0, 13.5, 1.0)  
        glRotatef(-5, 1, 0, 0)      
        glScalef(2.0, 5.0, 2.0)   
        glutSolidCube(1.0)
        glPopMatrix()
        
    
        glPushMatrix()
        glTranslatef(0, 18.5, 1.5)  
        glRotatef(-5, 1, 0, 0)      
        glScalef(0.9, 0.9, 0.9)
        draw_gun1()
        glPopMatrix()
        glPopMatrix()

       
        glPushMatrix()
        glTranslatef(3.5, 0.0, 18)   
        glRotatef(yaw_deg - 15, 0, 0, 1)  
        glRotatef(-10, 1, 0, 0)    
        glRotatef(-5, 0, 1, 0)     
        glColor3f(1.0, 0.85, 0.7)  
        
        
        glPushMatrix()
        glTranslatef(0, 3.0, 0)
        glScalef(1.8, 6.0, 1.8)     
        glutSolidCube(1.0)
        glPopMatrix()
        
        # Forearm segment
        glPushMatrix()
        glTranslatef(0, 8.0, 0)
        glScalef(1.5, 5.0, 1.5)     # Thicker forearm for better proportion
        glutSolidCube(1.0)
        glPopMatrix()
        
        # Right hand - extended length and thickness with better positioning
        glPushMatrix()
        glTranslatef(0, 13.5, 1.0)  # Positioned further out and slightly forward
        glRotatef(-5, 1, 0, 0)      # Slight angle for natural grip
        glScalef(2.0, 5.0, 2.0)    # Thicker hands for better proportion
        glutSolidCube(1.0)
        glPopMatrix()
        
        # Right gun (pistol)
        glPushMatrix()
        glTranslatef(0, 18.5, 1.5)  # Positioned at end of extended hand
        glRotatef(-5, 1, 0, 0)      # Match hand angle
        glScalef(0.8, 0.8, 0.8)
        draw_gun2()
        glPopMatrix()
        glPopMatrix()

        # Pop player root
        glPopMatrix()

def render_player_views():
    # Render player in three views: front, side, top
    player = Player((0,0,0))
    viewports = [
        (0, 0, WINDOW_W//3, WINDOW_H//2, 0, 0, 60, 'Front'),
        (WINDOW_W//3, 0, WINDOW_W//3, WINDOW_H//2, 90, 0, 60, 'Side'),
        (2*WINDOW_W//3, 0, WINDOW_W//3, WINDOW_H//2, 90, 90, 60, 'Top'),
    ]
    for vx, vy, vw, vh, rx, ry, dist, label in viewports:
        glViewport(vx, vy, vw, vh)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, vw/vh, 1, 200)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # Camera setup for each view
        glTranslatef(0, 0, -dist)
        glRotatef(rx, 1, 0, 0)
        glRotatef(ry, 0, 1, 0)
        player.draw()
        # Label
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, vw, 0, vh)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glColor3f(1,1,1)

        for ch in label:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18
import random
import time
import math


WINDOW_W, WINDOW_H = 1000, 800
ASPECT = WINDOW_W / WINDOW_H
FOVY = 74


Z_UP = (0, 0, 1)


camera_yaw = 0.0    
camera_pitch = 0.0  
CAMERA_ROTATION_SPEED = 4.7
MAX_PITCH = 84.0 
MIN_PITCH = -84.0  


GRID_HALF_X = 450         
CHUNK_LEN   = 360          
VISIBLE_CHUNKS_AHEAD = 4
VISIBLE_CHUNKS_BEHIND = 2

TREE_COUNT_PER_CHUNK   = (8, 15)
STONE_COUNT_PER_CHUNK  = (4, 8)
TRAP_COUNT_PER_CHUNK   = (2, 4)
FOOD_COUNT_PER_CHUNK   = (1, 3)
AMMO_COUNT_PER_CHUNK   = (1, 2)
WATER_COUNT_PER_CHUNK  = (1, 3)
ANIMAL_COUNT_PER_CHUNK = (3, 6)

CAMERA_SPEED_STEP = 27.0    
CAMERA_HEIGHT = 24.0       
PLAYER_SPEED = 24.0
JUMP_HEIGHT = 10.0
SPIN_SPEED = 34.0  # deg/sec for continuous showcase spin (medium)

# Player position and state
player_pos = {"x": 0.0, "y": 50.0, "z": 0.0}
player_jumping = False
jump_velocity = 0.0
in_water = False

# Weapon system
current_weapon = "left"  # Track which weapon is currently selected (left/right)
cheat_mode = False  # Cheat mode for continuous firing

# Health System
player_health = 100.0  # Start with 60 health to test food collection
max_health = 100.0
health_decrease_rate = 10.0  # Health lost when stepping on traps
health_increase_rate = 20.0  # Health gained when collecting food
last_damage_time = 0.0  # To prevent continuous damage
damage_cooldown = 2.0  # Seconds between damage instances

# Attack visual effects
attack_effect_active = False
attack_effect_start_time = 0.0
attack_effect_duration = 0.5  # Duration of visual effect in seconds
screen_shake_intensity = 0.0
screen_shake_duration = 0.0
health_flash_time = 0.0
damage_numbers = []  # List to store floating damage numbers

# Walking animation variables
walking_animation_time = 0.0
is_walking = False
walk_cycle_speed = 15.0  # Increased from 12.0 for even faster, more visible leg animation

# Cheat mode system - Super Power Implementation
# - Press 'G' to activate super power (once per game)
# - Super power provides 10 seconds of maximum speed with no obstacle collisions  
# - Player glows with golden pulsing effect when super power is active
# - Press 'R' or Backspace to restart game and reset super power availability
# - Press 'I' to check super power status and get help
cheat_mode_active = False
cheat_mode_used = False  # Can only be used once per game
cheat_mode_start_time = 0.0
cheat_mode_duration = 10.0  # 10 seconds of super power
cheat_activation_time = 0.0  # Time when cheat mode was activated

# Scoring system
game_start_time = time.time()
current_score = 0.0  # Score based on survival time
game_over = False

# Weather system variables
weather_start_time = time.time()
weather_cycle_duration = 10.0  # Each weather phase lasts 10 seconds
current_weather = "day"
weather_transition_time = 2.0  # 2 seconds for smooth transitions between weather states

# Weather states: day -> evening -> night -> early_morning -> day (clear weather)
# Then: day -> cloudy -> rain -> storm -> day (bad weather cycle)
weather_states = ["day", "evening", "night", "early_morning", "cloudy", "rain", "storm"]
weather_cycle = [
    # Clear weather cycle (4 phases × 10s = 40 seconds)
    "day", "evening", "night", "early_morning",
    # Bad weather cycle (3 phases × 10s = 30 seconds) 
    "cloudy", "rain", "storm"
]
weather_index = 0

# Rain and storm effects
rain_drops = []
thunder_flash_time = 0
thunder_flash_duration = 0.3

camera = {
    "x": 0.0, "y": 0.0, "z": CAMERA_HEIGHT,
    "fpv": True,
    "night_vision": False
}

# Player stats
player = {
    "health": 100,
    "max_health": 100,
    "rifle_ammo": 45,      # Separate ammo for rifle (left weapon)
    "pistol_ammo": 45,     # Separate ammo for pistol (right weapon)
    "last_shot_time": 0,
    "invulnerable_until": 0
}

# Animal types configuration (distinct size, vibrant color, and stats)
ANIMAL_TYPES = {
    "bear": {
    "size": 34, "health": 5, "damage": 30, "speed": 8, "detection_radius": 90,
    "attack_radius": 18, "color": (0.60, 0.25, 0.10), "secondary_color": (0.85, 0.55, 0.25),
    "accent_color": (1.0, 0.92, 0.75), "eye_color": (0.0, 0.0, 0.0)
    },
    "deer": {
    "size": 18, "health": 3, "damage": 15, "speed": 16, "detection_radius": 70,
    "attack_radius": 12, "color": (0.85, 0.40, 0.10), "secondary_color": (0.95, 0.85, 0.70),
    "accent_color": (0.60, 0.30, 0.05), "eye_color": (0.1, 0.05, 0.0)
    },
    "fox": {
        "size": 8, "health": 1, "damage": 10, "speed": 20, "detection_radius": 65,
        "attack_radius": 9, "color": (1.00, 0.40, 0.00), "secondary_color": (1.00, 0.85, 0.30),
        "accent_color": (1.0, 1.0, 1.0), "eye_color": (0.15, 0.55, 1.0)
    }
}


foods   = []  
ammos   = []  
traps   = []  
stones  = []  
waters  = [] 
animals = []  # List of all active animals
bullets = []  # List of active bullets 

chunks = {}
last_generated_chunk = -1

game_paused = False
rand = random.Random()

def clamp(v, a, b):
    return max(a, min(b, v))

def check_animal_player_collision(animal_x, animal_y, animal_size):
    """Check if animal position would collide with player"""
    player_x, player_y = player_pos["x"], player_pos["y"]
    
    # Player collision radius (scaled player size)
    player_radius = 8.0  # Player body radius
    animal_radius = animal_size * 0.6  # Animal collision radius
    
    # Calculate distance between animal and player
    distance = math.sqrt((animal_x - player_x)**2 + (animal_y - player_y)**2)
    
    # Check if they would overlap
    min_distance = player_radius + animal_radius
    return distance < min_distance



def check_animal_animal_collision(animal1, animal_x, animal_y):
    """Check if animal position would collide with other animals"""
    animal1_size = ANIMAL_TYPES[animal1["type"]]["size"]
    animal1_radius = animal1_size * 0.6
    
    for animal2 in animals:
        # Don't check collision with itself
        if animal1 is animal2:
            continue
            
        # Skip dead animals
        if animal2["state"] == "dead":
            continue
            
        animal2_size = ANIMAL_TYPES[animal2["type"]]["size"]
        animal2_radius = animal2_size * 0.6
        
        # Calculate distance between animals
        distance = math.sqrt((animal_x - animal2["x"])**2 + (animal_y - animal2["y"])**2)
        
        # Check if they would overlap
        min_distance = animal1_radius + animal2_radius
        if distance < min_distance:
            return True
            
    return False

def get_valid_animal_position(animal, new_x, new_y):
    """Get a valid position for animal that doesn't collide with player or other animals"""
    original_x, original_y = animal["x"], animal["y"]
    
    # Check if new position would cause collisions
    animal_size = ANIMAL_TYPES[animal["type"]]["size"]
    
    # Check collision with player
    if check_animal_player_collision(new_x, new_y, animal_size):
        # Try to find alternative position by moving around the player
        player_x, player_y = player_pos["x"], player_pos["y"]
        
        # Calculate direction from player to animal
        dx = original_x - player_x
        dy = original_y - player_y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 0:
            # Push animal away from player
            push_distance = animal_size + 12.0  # Safe distance
            new_x = player_x + (dx / distance) * push_distance
            new_y = player_y + (dy / distance) * push_distance
    
    # Check collision with other animals
    if check_animal_animal_collision(animal, new_x, new_y):
        # Try to find alternative position by slightly adjusting movement
        for angle_offset in [30, -30, 60, -60, 90, -90]:
            angle = math.radians(angle_offset)
            offset_x = math.cos(angle) * 10.0
            offset_y = math.sin(angle) * 10.0
            
            test_x = new_x + offset_x
            test_y = new_y + offset_y
            
            # Check if this adjusted position is valid
            if not check_animal_animal_collision(animal, test_x, test_y) and \
               not check_animal_player_collision(test_x, test_y, animal_size):
                new_x, new_y = test_x, test_y
                break
        else:
            # If no valid position found, keep original position
            new_x, new_y = original_x, original_y
    
    return new_x, new_y

def check_comprehensive_obstacle_collision(x, y):
    """
    Comprehensive obstacle detection for trees, animals, and big stones.
    Returns True if movement is allowed, False if blocked by obstacles.
    Uses only authorized functions from attached files.
    """
    # Check ALL stones (both big and small stones block movement to prevent overlapping)
    for stone in stones:
        stone_x, stone_y = stone["x"], stone["y"]
        stone_size = stone["size"]
        
        # Calculate distance using math.sqrt (from Lets_draw_sth.py)
        distance = math.sqrt((x - stone_x)**2 + (y - stone_y)**2)
        
        # Safe collision radius - player stops at safe distance before stone
        # Add player radius (3.0) + stone radius + safety margin (2.0)
        safe_collision_radius = stone_size + 3.0 + 2.0
        
        if distance < safe_collision_radius:
            if not stone["is_small"]:  # Big stones can be jumped over
                if not player_jumping:
                    print("Big stone ahead! Press SPACE to jump over it.")
                    return False
                else:
                    # Even when jumping, need to be high enough to clear the stone
                    if jump_velocity <= 8.0:
                        print("Jump higher to clear the big stone!")
                        return False
            else:  # Small stones block movement completely - no jumping over them
                print("Small stone blocking! Cannot pass through.")
                return False
    
    # Check trees - ALL trees are solid obstacles
    camera_chunk = int(camera["y"] // CHUNK_LEN)
    for chunk_offset in range(-VISIBLE_CHUNKS_BEHIND, VISIBLE_CHUNKS_AHEAD + 1):
        chunk_idx = camera_chunk + chunk_offset
        if chunk_idx in chunks:
            chunk = chunks[chunk_idx]
            for tree_data in chunk["trees"]:
                if len(tree_data) == 3:  
                    tree_x, tree_y, tree_type = tree_data
                else:
                    tree_x, tree_y = tree_data
                    tree_type = 0  
                
                # Calculate distance using math.sqrt (from Lets_draw_sth.py)
                distance = math.sqrt((x - tree_x)**2 + (y - tree_y)**2)
                
                # All tree types are solid obstacles - no jumping over trees
                # Safe collision radius - player stops at safe distance before tree
                # Add player radius (3.0) + tree radius (7.5) + safety margin (1.5)
                safe_tree_radius = 7.5 + 3.0 + 1.5
                if distance < safe_tree_radius:
                    print("Tree blocking! Cannot pass through.")
                    return False
    
    # Check animals - ALL animals are solid obstacles
    for animal in animals:
        animal_x, animal_y = animal["x"], animal["y"]
        animal_size = animal["config"]["size"]
        
        # Calculate distance using math.sqrt (from Lets_draw_sth.py)
        distance = math.sqrt((x - animal_x)**2 + (y - animal_y)**2)
        
        # All animals are solid obstacles - no jumping over animals
        # Safe collision radius - player stops at safe distance before animal
        # Add player radius (3.0) + animal radius + safety margin (1.5)
        safe_collision_radius = (animal_size * 0.7) + 3.0 + 1.5
        if distance < safe_collision_radius:
            print("Animal blocking! Cannot pass through.")
            return False
    
    return True  # No obstacles detected, movement allowed

def check_stone_ground_height(x, y):
    """Check stone collision for ground height calculation only"""
    ground_height = 0.0
    for stone in stones:
        stone_x, stone_y = stone["x"], stone["y"]
        stone_size = stone["size"]
        distance = math.sqrt((x - stone_x)**2 + (y - stone_y)**2)
        
        # Calculate ground height for both small and big stones
        if distance < stone_size * 0.8:
            ground_height = max(ground_height, stone_size * 0.6)
    
    return ground_height



def check_trap_collision(x, y):
    """Check if player steps on a trap and apply damage"""
    global player_health, last_damage_time
    import time
    
    current_time = time.time()
    
    for trap in traps:
        trap_x, trap_y = trap["x"], trap["y"]
        trap_w, trap_l = trap["w"], trap["l"]
        
        # Check if player is within trap bounds
        if (abs(x - trap_x) < trap_w/2 and abs(y - trap_y) < trap_l/2):
            # Apply damage if cooldown period has passed
            if current_time - last_damage_time > damage_cooldown:
                player_health -= health_decrease_rate
                player_health = max(0, player_health)  # Don't go below 0
                last_damage_time = current_time
                print(f"Stepped on trap! Health: {player_health}")
            return True
    return False

def trigger_attack_effect(damage_amount):
    """Trigger visual effects when player is attacked"""
    global attack_effect_active, attack_effect_start_time, screen_shake_intensity
    global screen_shake_duration, health_flash_time, damage_numbers
    
    current_time = time.time()
    attack_effect_active = True
    attack_effect_start_time = current_time
    screen_shake_intensity = 10.0  # Intensity of screen shake
    screen_shake_duration = 0.3   # Duration of screen shake
    health_flash_time = current_time + 0.5  # Flash health bar for 0.5 seconds
    
    # Add floating damage number
    damage_numbers.append({
        'damage': damage_amount,
        'start_time': current_time,
        'x': player_pos["x"] + random.uniform(-20, 20),
        'y': player_pos["y"] + random.uniform(-20, 20),
        'z': 5
    })

def update_attack_effects():
    """Update visual attack effects"""
    global attack_effect_active, screen_shake_intensity, screen_shake_duration
    global damage_numbers
    
    current_time = time.time()
    
    # Update screen shake
    if screen_shake_duration > 0:
        screen_shake_duration -= 0.016  # Approximate frame time
        if screen_shake_duration <= 0:
            screen_shake_intensity = 0
    
    # Update attack effect
    if attack_effect_active and current_time - attack_effect_start_time > attack_effect_duration:
        attack_effect_active = False
    
    # Update damage numbers (remove old ones)
    damage_numbers = [num for num in damage_numbers if current_time - num['start_time'] < 2.0]

def apply_screen_shake():
    """Apply screen shake effect to camera"""
    if screen_shake_intensity > 0:
        shake_x = random.uniform(-screen_shake_intensity, screen_shake_intensity)
        shake_y = random.uniform(-screen_shake_intensity, screen_shake_intensity)
        glTranslatef(shake_x, shake_y, 0)

def draw_attack_effects():
    """Draw visual attack effects"""
    current_time = time.time()
    
    # Draw damage numbers
    for damage_num in damage_numbers:
        age = current_time - damage_num['start_time']
        if age < 2.0:  # Show for 2 seconds
            alpha = 1.0 - (age / 2.0)  # Fade out
            y_offset = age * 50  # Float upward
            
            glColor3f(1.0, 0.2, 0.2)  # Red damage text
            draw_text_3d(f"-{int(damage_num['damage'])}", 
                         damage_num['x'], damage_num['y'] + y_offset, damage_num['z'])
    
    # Draw screen flash effect when attacked
    if attack_effect_active:
        effect_age = current_time - attack_effect_start_time
        if effect_age < attack_effect_duration:
            # Red screen flash
            flash_intensity = (1.0 - effect_age / attack_effect_duration) * 0.3
            
            # Switch to 2D rendering for screen overlay
            glMatrixMode(GL_PROJECTION)
            glPushMatrix()
            glLoadIdentity()
            gluOrtho2D(0, WINDOW_W, 0, WINDOW_H)
            glMatrixMode(GL_MODELVIEW)
            glPushMatrix()
            glLoadIdentity()
            
            glColor4f(1.0, 0.0, 0.0, flash_intensity)  # Red flash
            
            glBegin(GL_QUADS)
            glVertex2f(0, 0)
            glVertex2f(WINDOW_W, 0)
            glVertex2f(WINDOW_W, WINDOW_H)
            glVertex2f(0, WINDOW_H)
            glEnd()
            
            glDisable(GL_BLEND)
            
            # Restore 3D rendering
            glPopMatrix()
            glMatrixMode(GL_PROJECTION)
            glPopMatrix()
            glMatrixMode(GL_MODELVIEW)

def check_food_collision(x, y):
    """Check if player collects food and restore health"""
    global player_health, foods
    
    # Only collect one food item per update to prevent multiple collections
    for i in range(len(foods) - 1, -1, -1):
        food = foods[i]
        food_x, food_y = food["x"], food["y"]
        
        # Food collision radius
        food_radius = 16.0
        distance = math.sqrt((x - food_x)**2 + (y - food_y)**2)
        
        # If player is close enough to collect food
        if distance < food_radius:
            # Restore health (add exactly the health_increase_rate amount)
            old_health = player_health
            player_health += health_increase_rate
            player_health = min(max_health, player_health)  # Don't exceed max health
            actual_increase = player_health - old_health
            print(f"Collected food! Health: {old_health} -> {player_health} (+{actual_increase})")
            
            # Remove the collected food from global list
            foods.pop(i)
            
            # Remove from chunks too
            for chunk in chunks.values():
                for j in range(len(chunk["foods"]) - 1, -1, -1):
                    chunk_food = chunk["foods"][j]
                    if chunk_food["x"] == food_x and chunk_food["y"] == food_y:
                        chunk["foods"].pop(j)
                        break
            
            return True  # Return immediately after collecting one food item
    return False

def check_ammo_collision(x, y):
    """Check if player walks over ammo and automatically collect it"""
    global player, ammos
    
    # Only collect one ammo box per update to prevent multiple collections
    for i in range(len(ammos) - 1, -1, -1):
        ammo_box = ammos[i]
        ammo_x, ammo_y = ammo_box["x"], ammo_box["y"]
        
        # Ammo collision radius
        ammo_radius = 20.0
        distance = math.sqrt((x - ammo_x)**2 + (y - ammo_y)**2)
        
        # If player is close enough to collect ammo
        if distance < ammo_radius:
            # Increase both weapon ammo types
            old_rifle = player["rifle_ammo"]
            old_pistol = player["pistol_ammo"]
            player["rifle_ammo"] += ammo_box["amount"]
            player["pistol_ammo"] += ammo_box["amount"]
            
            print(f"Collected {ammo_box['amount']} ammo! Rifle: {old_rifle} -> {player['rifle_ammo']}, Pistol: {old_pistol} -> {player['pistol_ammo']}")
            
            # Remove the collected ammo from global list
            ammos.pop(i)
            
            # Remove from chunks too
            for chunk in chunks.values():
                for j in range(len(chunk["ammos"]) - 1, -1, -1):
                    chunk_ammo = chunk["ammos"][j]
                    if chunk_ammo["x"] == ammo_x and chunk_ammo["y"] == ammo_y:
                        chunk["ammos"].pop(j)
                        break
            
            return True  # Return immediately after collecting one ammo box
    return False

def check_water_collision(x, y):
    """Check if player is in water and return depth"""
    for water in waters:
        water_x, water_y = water["x"], water["y"]
        water_w, water_l = water["w"], water["l"]
        
        # Check if player is within water bounds
        if (abs(x - water_x) < water_w/2 and abs(y - water_y) < water_l/2):
            # Calculate distance from water center for depth effect
            distance_from_center = math.sqrt((x - water_x)**2 + (y - water_y)**2)
            max_distance = min(water_w, water_l) / 2
            depth_factor = 1.0 - (distance_from_center / max_distance)
            # More pronounced sinking - deeper in center, shallower at edges
            sink_depth = depth_factor * 8.0  # Max sink depth of 8 units (doubled)
            return True, sink_depth
    return False, 0.0

def update_player_physics():
    """Update player physics including jumping and gravity"""
    global player_jumping, jump_velocity, in_water
    
    # Check water collision with depth
    in_water_result, water_depth = check_water_collision(player_pos["x"], player_pos["y"])
    in_water = in_water_result
    
    # Check health-related collisions
    check_trap_collision(player_pos["x"], player_pos["y"])
    check_food_collision(player_pos["x"], player_pos["y"])
    
    # Check for automatic ammo collection
    check_ammo_collision(player_pos["x"], player_pos["y"])
    
    # Check stone collision and get ground height using new system
    ground_height = check_stone_ground_height(player_pos["x"], player_pos["y"])
    
    # Apply water depth effect (sinking)
    if in_water:
        # Sink deeper into water - this makes it harder to move
        ground_height = ground_height - water_depth  # Sink into water
        # Slow down movement in water
        global PLAYER_SPEED
        if not hasattr(update_player_physics, 'original_speed'):
            update_player_physics.original_speed = PLAYER_SPEED
        PLAYER_SPEED = update_player_physics.original_speed * 0.6  # 40% slower in water
    else:
        # Restore normal speed on land
        if hasattr(update_player_physics, 'original_speed'):
            PLAYER_SPEED = update_player_physics.original_speed
    
    if player_jumping:
        # Apply gravity
        gravity = 0.8
        if in_water:
            gravity *= 0.7  # Reduced gravity in water for more realistic physics
        jump_velocity -= gravity
        player_pos["z"] += jump_velocity
        
        # Land on ground or stone (or water surface)
        if player_pos["z"] <= ground_height:
            player_pos["z"] = ground_height
            player_jumping = False
            jump_velocity = 0.0
    else:
        # Keep player on ground/stone/water level
        player_pos["z"] = ground_height

def move_player(direction):
    """Move player in specified direction relative to camera"""
    global player_jumping, jump_velocity, is_walking, walking_animation_time
    global cheat_mode_active, cheat_activation_time, cheat_mode_duration
    
    # Prevent movement if player is dead
    if player_health <= 0:
        return
    
    # Check if cheat mode should be deactivated
    if cheat_mode_active:
        if time.time() - cheat_activation_time >= cheat_mode_duration:
            cheat_mode_active = False
            print("Super power ended! Back to normal movement.")
    
    yaw_rad = math.radians(camera_yaw)
    old_x, old_y = player_pos["x"], player_pos["y"]
    
    # Use maximum speed during cheat mode
    current_speed = PLAYER_SPEED * 3.0 if cheat_mode_active else PLAYER_SPEED
    
    if direction == "forward":
        new_x = player_pos["x"] + current_speed * math.sin(yaw_rad)
        new_y = player_pos["y"] + current_speed * math.cos(yaw_rad)
    elif direction == "backward":
        new_x = player_pos["x"] - current_speed * math.sin(yaw_rad)
        new_y = player_pos["y"] - current_speed * math.cos(yaw_rad)
    elif direction == "left":
        new_x = player_pos["x"] - current_speed * math.cos(yaw_rad)
        new_y = player_pos["y"] + current_speed * math.sin(yaw_rad)
    elif direction == "right":
        new_x = player_pos["x"] + current_speed * math.cos(yaw_rad)
        new_y = player_pos["y"] - current_speed * math.sin(yaw_rad)
    else:
        return
    
    # Super power mode: ignore all obstacles
    if cheat_mode_active:
        player_pos["x"] = clamp(new_x, -GRID_HALF_X+5, GRID_HALF_X-5)
        player_pos["y"] = new_y
        is_walking = True
        walking_animation_time += walk_cycle_speed * 0.15  # Faster animation during cheat mode
        update_player_physics()
        return
    
    # Normal movement: Use comprehensive obstacle detection
    can_move = check_comprehensive_obstacle_collision(new_x, new_y)
    
    # Apply movement if no obstacles detected
    if can_move:
        player_pos["x"] = clamp(new_x, -GRID_HALF_X+5, GRID_HALF_X-5)
        player_pos["y"] = new_y
        is_walking = True
        walking_animation_time += walk_cycle_speed * 0.1
    # If movement blocked, player stays in place (no movement)
    
    update_player_physics()

def jump_player():
    """Make player jump - stronger jump when in water to help escape"""
    global player_jumping, jump_velocity, in_water
    if not player_jumping:
        player_jumping = True
        # Much stronger jump when in water to help escape the sinking effect
        if in_water:
            jump_velocity = JUMP_HEIGHT * 2.0  # Double jump power in water
            print("Strong water jump activated!")  # Debug feedback
        else:
            jump_velocity = JUMP_HEIGHT

def switch_weapon():
    """Switch between left and right weapons"""
    global current_weapon
    if current_weapon == "left":
        current_weapon = "right"
        print("Switched to RIGHT weapon (Pistol - Red bullets)")
    else:
        current_weapon = "left"
        print("Switched to LEFT weapon (Rifle - Blue bullets)")

def now():
    return time.time()

def update_weather():
    """Update the current weather state based on time progression"""
    global current_weather, weather_index, weather_start_time, thunder_flash_time, rain_drops
    
    current_time = now()
    elapsed_time = current_time - weather_start_time
    
    # Check if it's time to advance to next weather state
    if elapsed_time >= weather_cycle_duration:
        weather_start_time = current_time
        weather_index = (weather_index + 1) % len(weather_cycle)
        current_weather = weather_cycle[weather_index]
        
        # Initialize rain drops when entering rain/storm states
        if current_weather in ["rain", "storm"]:
            rain_drops = []
            for i in range(200 if current_weather == "rain" else 400):
                rain_drops.append({
                    "x": random.uniform(-200, 200),
                    "y": random.uniform(-200, 200), 
                    "z": random.uniform(20, 100),
                    "speed": random.uniform(40, 80) if current_weather == "rain" else random.uniform(60, 120),
                    "length": random.uniform(2, 4) if current_weather == "rain" else random.uniform(3, 6)
                })
        else:
            rain_drops = []
    
    # Update rain drops
    if current_weather in ["rain", "storm"]:
        dt = 0.016  # Approximate frame time
        for drop in rain_drops:
            drop["z"] -= drop["speed"] * dt
            # Reset rain drop when it hits ground
            if drop["z"] <= 0:
                drop["x"] = random.uniform(-200, 200)
                drop["y"] = random.uniform(-200, 200)
                drop["z"] = random.uniform(80, 120)
    
    # Handle thunder flash timing - removed since thunder_storm is removed
    # Thunder storm functionality has been disabled

def get_weather_background_color():
    """Get the background color based on current weather and time"""
    current_time = now()
    elapsed_time = current_time - weather_start_time
    transition_progress = min(1.0, elapsed_time / weather_transition_time)
    
    # Define base colors for each weather state
    weather_colors = {
        "day": (0.53, 0.78, 1.0),           # Bright blue sky
        "evening": (1.0, 0.6, 0.3),         # Orange/pink sunset
        "night": (0.1, 0.1, 0.3),           # Dark blue night
        "early_morning": (0.7, 0.8, 0.9),   # Light blue morning
        "cloudy": (0.6, 0.6, 0.7),          # Gray cloudy
        "rain": (0.4, 0.4, 0.5),            # Darker gray for rain
        "storm": (0.35, 0.35, 0.45)         # Dark but not too dark for storm (improved visibility)
    }
    
    base_color = weather_colors.get(current_weather, weather_colors["day"])
    
    # Thunder storm functionality removed - no more lightning effects
    return base_color

def get_weather_lighting_modifier():
    """Get lighting modifier based on current weather for realistic atmosphere"""
    weather_lighting = {
        "day": (1.0, 1.0, 1.0),           # Normal bright lighting
        "evening": (1.1, 0.8, 0.6),       # Warm evening light
        "night": (0.3, 0.3, 0.5),         # Very dim blue lighting
        "early_morning": (0.8, 0.9, 1.0), # Cool morning light
        "cloudy": (0.7, 0.7, 0.7),        # Dim gray lighting
        "rain": (0.5, 0.5, 0.6),          # Dark and cool
        "storm": (0.6, 0.6, 0.7)          # Dark but still visible (improved from 0.3, 0.3, 0.4)
    }
    
    base_modifier = weather_lighting.get(current_weather, (1.0, 1.0, 1.0))
    
    # Thunder storm functionality removed - no more lightning effects
    return base_modifier

def apply_weather_lighting(r, g, b):
    """Apply weather-based lighting modification to colors"""
    modifier = get_weather_lighting_modifier()
    return (
        min(1.0, r * modifier[0]),
        min(1.0, g * modifier[1]), 
        min(1.0, b * modifier[2])
    )

def draw_rain_effects():
    """Draw rain drops and storm effects"""
    if current_weather not in ["rain", "storm"]:
        return
    
    glPushMatrix()
    # Position rain relative to camera
    glTranslatef(camera["x"], camera["y"], 0)
    
    # Draw rain drops
    if current_weather == "rain":
        glColor3f(0.7, 0.7, 0.9)  # Light blue rain
    else:  # storm
        glColor3f(0.5, 0.5, 0.7)  # Darker rain
    
    glLineWidth(1.0 if current_weather == "rain" else 2.0)
    
    # Draw rain drops as lines
    glBegin(GL_LINES)
    for drop in rain_drops:
        x, y, z = drop["x"], drop["y"], drop["z"]
        length = drop["length"]
        
        glVertex3f(x, y, z)
        glVertex3f(x, y - length, z - length)
    glEnd()
    
    glPopMatrix()
    
    # Storm atmospheric effects removed to avoid hiding game elements
    # Storm weather will only be indicated by:
    # 1. Darker background color (handled in get_weather_background_color)
    # 2. Heavier rain drops (handled above)
    # 3. Weather lighting modifier (handled in get_weather_lighting_modifier)
    # No fog/mist effects that could hide players, animals, or environment

def screen_text(x, y, text):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_W, 0, WINDOW_H)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def draw_text_3d(text, x, y, z):
    """Draw 3D text at world coordinates"""
    glPushMatrix()
    glTranslatef(x, y, z)
    # Make text face the camera using the global camera_yaw variable
    glRotatef(-camera_yaw, 0, 0, 1)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glPopMatrix()

def draw_floor_grid():
   
    ground_color = (0.35, 0.6, 0.3)  
    glColor3f(*ground_color)
    
    camera_chunk = int(camera["y"] // CHUNK_LEN)
    minx, maxx = -GRID_HALF_X - 100, GRID_HALF_X + 100
    y0 = (camera_chunk - VISIBLE_CHUNKS_BEHIND - 2) * CHUNK_LEN
    y1 = (camera_chunk + VISIBLE_CHUNKS_AHEAD + 4) * CHUNK_LEN
    
    glBegin(GL_QUADS)
    glVertex3f(minx, y0, 0)
    glVertex3f(maxx, y0, 0)
    glVertex3f(maxx, y1, 0)
    glVertex3f(minx, y1, 0)
    glEnd()
    
   
    glColor3f(ground_color[0] * 0.9, ground_color[1] * 0.9, ground_color[2] * 0.9)
    glLineWidth(1)
    
    glBegin(GL_LINES)
    
    for x in range(int(minx), int(maxx), 100):
        glVertex3f(x, y0, 0.1)
        glVertex3f(x, y1, 0.1)
    
    
    for y in range(int(y0), int(y1), 100):
        glVertex3f(minx, y, 0.1)
        glVertex3f(maxx, y, 0.1)
    glEnd()

def draw_tree(x, y, tree_type=0):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glColor3f(0.4, 0.2, 0.1)
    quad = gluNewQuadric()
    gluQuadricDrawStyle(quad, GLU_FILL)
    gluCylinder(quad, 6, 4, 40, 16, 8)
    glColor3f(0.3, 0.15, 0.08)
    for i in range(4):
        glPushMatrix()
        glTranslatef(0, 0, 10 + i * 8)
        glRotatef(90, 1, 0, 0)
        ring_quad = gluNewQuadric()
        gluQuadricDrawStyle(ring_quad, GLU_FILL)
        gluCylinder(ring_quad, 5.8, 6.4, 1.0, 16, 4)
        glPopMatrix()
    
    glColor3f(0.3, 0.15, 0.08)
    for branch in [(-8, -4, 30, 15), (6, 9, 35, -20), (-4, 10, 40, 45)]:
        glPushMatrix()
        glTranslatef(0, 0, branch[2])
        glRotatef(branch[3], 0, 0, 1)
        glRotatef(45, 1, 0, 0)
        branch_quad = gluNewQuadric()
        gluQuadricDrawStyle(branch_quad, GLU_FILL)
        gluCylinder(branch_quad, 1.2, 0.6, 10, 12, 4)
        glPopMatrix()
    
    if tree_type == 0:
        secondary_foliage_color = (0.15, 0.6, 0.15)
        main_foliage_color = (0.1, 0.5, 0.1)
    else:
        secondary_foliage_color = (0.5, 0.8, 0.3)  
        main_foliage_color = (0.7, 0.9, 0.4)      
    
    for offset in [(-10, -6, 38), (8, 10, 42), (-5, 12, 48), (11, -4, 52)]:
        glPushMatrix()
        glTranslatef(offset[0], offset[1], offset[2])
        glColor3f(*secondary_foliage_color)
        for rotation in [(0, 0, 0), (22.5, 0, 0), (45, 0, 0), (0, 22.5, 0), (0, 45, 0)]:
            glPushMatrix()
            glRotatef(rotation[0], 1, 0, 0)
            glRotatef(rotation[1], 0, 1, 0)
            glRotatef(rotation[2], 0, 0, 1)
            glScalef(1.2, 1.2, 1.2)
            glutSolidCube(12)
            glPopMatrix()
        glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 0, 45)
    glColor3f(*main_foliage_color)
    for dx in [-8, 0, 8]:
        for dy in [-8, 0, 8]:
            for dz in [-8, 0, 8]:
                glPushMatrix()
                glTranslatef(dx, dy, dz)
                glRotatef(dx * 5, 1, 0, 0)
                glRotatef(dy * 5, 0, 1, 0)
                glRotatef(dz * 5, 0, 0, 1)
                glutSolidCube(10)
                glPopMatrix()
    if tree_type == 1:
        glColor3f(1.0, 1.0, 0.6)  
        for highlight_pos in [(-4, -4, 4), (4, 4, -4), (0, -6, 2), (6, 0, -2)]:
            glPushMatrix()
            glTranslatef(highlight_pos[0], highlight_pos[1], highlight_pos[2])
            glutSolidCube(6)
            glPopMatrix()
    
    glPopMatrix()
    
    glPopMatrix()

def draw_stone(stone_data):
    x, y = stone_data["x"], stone_data["y"]
    size = stone_data["size"]
    height = stone_data["height"]
    is_small = stone_data["is_small"]
    
    glPushMatrix()
    glTranslatef(x, y, 0)
    
    if is_small:
        rock_colors = [(0.6, 0.55, 0.5), (0.65, 0.6, 0.55), (0.7, 0.65, 0.6)]

        glPushMatrix()
        glTranslatef(0, 0, size * 0.4)
        glColor3f(*rock_colors[0])
        gluSphere(gluNewQuadric(), size * 0.3, 8, 6)
        glPopMatrix()
    
        for i, (dx, dy, dz) in enumerate([(-size*0.2, size*0.15, size*0.2), 
                                          (size*0.25, -size*0.1, size*0.15),
                                          (-size*0.1, -size*0.2, size*0.25)]):
            glPushMatrix()
            glTranslatef(dx, dy, dz)
            glColor3f(*rock_colors[i % len(rock_colors)])
            gluSphere(gluNewQuadric(), size * 0.15, 6, 4)
            glPopMatrix()
            
    else:
        boulder_colors = [(0.45, 0.4, 0.35), (0.5, 0.45, 0.4), (0.55, 0.5, 0.45), (0.4, 0.35, 0.3)]
        
        glPushMatrix()
        glTranslatef(0, 0, size * 0.6)  
        glColor3f(*boulder_colors[0])
        gluSphere(gluNewQuadric(), size * 0.5, 12, 10)  
        glPopMatrix()
        positions = [(-size*0.4, -size*0.25, size*0.4), (size*0.45, size*0.15, size*0.35),
                    (-size*0.15, size*0.5, size*0.45), (size*0.25, -size*0.45, size*0.5)]
        
        for i, (dx, dy, dz) in enumerate(positions):
            glPushMatrix()
            glTranslatef(dx, dy, dz)
            glColor3f(*boulder_colors[i % len(boulder_colors)])
            gluSphere(gluNewQuadric(), size * 0.3, 10, 8)  
            glPopMatrix()
    
    glPopMatrix()

def draw_trap(t):
    x, y, w, l = t["x"], t["y"], t["w"], t["l"]
    
    glPushMatrix()
    glTranslatef(x, y, 0)
    
    glColor3f(0.2, 0.1, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(-w/2, -l/2, 0.1)
    glVertex3f(w/2, -l/2, 0.1)
    glVertex3f(w/2, l/2, 0.1)
    glVertex3f(-w/2, l/2, 0.1)
    glEnd()
    
    current_time = time.time()
    flame_flicker = math.sin(current_time * 8) * 0.3
    
    flame_data = [
        (0, 0, 15 + flame_flicker, 1.0, 0.3, 0.0, 1.0),
        (-5, 3, 12 + flame_flicker * 0.7, 1.0, 0.5, 0.0, 0.8),
        (4, -2, 10 + flame_flicker * 0.5, 1.0, 0.7, 0.1, 0.7),
        (-2, -4, 8 + flame_flicker * 0.8, 1.0, 0.8, 0.2, 0.6),
        (6, 5, 13 + flame_flicker * 0.6, 0.9, 0.2, 0.1, 0.9),
    ]
    
    for fx, fy, fh, r, g, b, scale in flame_data:
        for i in range(3):
            angle_offset = i * 120
            triangle_x = fx + math.cos(math.radians(angle_offset)) * 2 * scale
            triangle_y = fy + math.sin(math.radians(angle_offset)) * 2 * scale
            
            glBegin(GL_TRIANGLES)
            glColor3f(r, g, b)
            base_width = 4 * scale
            glVertex3f(triangle_x - base_width, triangle_y, 1)
            glVertex3f(triangle_x + base_width, triangle_y, 1)
            glVertex3f(triangle_x, triangle_y, fh)
            glEnd()
    
    for i in range(5):
        angle = i * 72
        core_x = math.cos(math.radians(angle)) * 3
        core_y = math.sin(math.radians(angle)) * 3
        core_height = 8 + flame_flicker * 0.4
        
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 1.0, 0.3)
        glVertex3f(core_x - 1.5, core_y, 1)
        glVertex3f(core_x + 1.5, core_y, 1)
        glVertex3f(core_x, core_y, core_height)
        glEnd()
    
    for i in range(8):
        ember_time = current_time + i * 0.5
        ember_height = 5 + (ember_time % 10) * 2
        ember_x = math.cos(ember_time) * 6
        ember_y = math.sin(ember_time * 1.3) * 6
        
        glPushMatrix()
        glTranslatef(ember_x, ember_y, ember_height)
        glColor3f(1.0, 0.4, 0.1)
        gluSphere(gluNewQuadric(), 0.5, 4, 3)
        glPopMatrix()
    
    glPopMatrix()

def draw_food(f):
    glPushMatrix()
    glTranslatef(f["x"], f["y"], 0)
    glPushMatrix()
    glTranslatef(0, 0, 3)
    glColor3f(0.8, 0.6, 0.4)
    glScalef(1.0, 1.0, 0.4)
    gluSphere(gluNewQuadric(), 8, 10, 6)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, 0, 6)
    glColor3f(0.2, 0.8, 0.3)
    glScalef(1.1, 1.1, 0.2)
    gluSphere(gluNewQuadric(), 7, 8, 4)
    glPopMatrix()
    
    
    glPushMatrix()
    glTranslatef(0, 0, 8)
    glColor3f(0.6, 0.3, 0.2)
    glScalef(0.9, 0.9, 0.5)
    gluSphere(gluNewQuadric(), 7, 8, 6)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 0, 10)
    glColor3f(1.0, 0.9, 0.3)
    glScalef(1.0, 1.0, 0.15)
    gluSphere(gluNewQuadric(), 7.5, 8, 4)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 0, 11)
    glColor3f(0.9, 0.2, 0.2)
    glScalef(0.8, 0.8, 0.2)
    gluSphere(gluNewQuadric(), 6, 8, 4)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 0, 14)
    glColor3f(0.85, 0.65, 0.45)
    glScalef(1.0, 1.0, 0.6)
    gluSphere(gluNewQuadric(), 8, 10, 6)
    glPopMatrix()
    
    for i, (dx, dy) in enumerate([(-2, 1), (3, -1), (-1, -2), (1, 2), (-3, 0)]):
        glPushMatrix()
        glTranslatef(dx, dy, 17)
        glColor3f(0.95, 0.95, 0.9)
        gluSphere(gluNewQuadric(), 0.5, 4, 3)
        glPopMatrix()
    
    glPopMatrix()

def draw_ammo(a):
   
    glPushMatrix()
    glTranslatef(a["x"], a["y"], 0)
    
    glPushMatrix()
    glTranslatef(0, 0, 4)
    glColor3f(0.4, 0.3, 0.2)
    glutSolidCube(10)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, 0, 9)
    glColor3f(0.5, 0.4, 0.25)
    glScalef(0.9, 0.9, 0.3)
    glutSolidCube(10)
    glPopMatrix()
    
    bullet_positions = [(-3, -3, 12), (0, -3, 12), (3, -3, 12), 
                       (-1.5, 0, 12), (1.5, 0, 12)]
    
    for i, (bx, by, bz) in enumerate(bullet_positions):
        glPushMatrix()
        glTranslatef(bx, by, bz)
        glColor3f(0.8, 0.7, 0.3)
        gluCylinder(gluNewQuadric(), 1, 1, 4, 6, 2)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(bx, by, bz + 4)
        glColor3f(0.6, 0.6, 0.65)
        gluSphere(gluNewQuadric(), 1.2, 6, 4)
        glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 5.1, 6)
    glColor3f(0.9, 0.9, 0.1)
    glScalef(4, 0.1, 1)
    glutSolidCube(1)
    glPopMatrix()
    
    glPopMatrix()

def draw_water(wt):
    x, y, w, l = wt["x"], wt["y"], wt["w"], wt["l"]
    
    glPushMatrix()
    glTranslatef(x, y, 0)
    
    pond_radius = min(w, l) / 2.0
    
    glColor3f(0.4, 0.3, 0.2)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0.1)
    for i in range(33):
        angle = i * 2 * math.pi / 32
        shore_radius = pond_radius + 3
        px = shore_radius * math.cos(angle)
        py = shore_radius * math.sin(angle)
        glVertex3f(px, py, 0.1)
    glEnd()
    
    current_time = time.time()
    water_ripple = math.sin(current_time * 2) * 0.1
    
    glColor3f(0.1, 0.3, 0.7)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0.2 + water_ripple)
    for i in range(33):
        angle = i * 2 * math.pi / 32
        px = pond_radius * 0.6 * math.cos(angle)
        py = pond_radius * 0.6 * math.sin(angle)
        glVertex3f(px, py, 0.2 + water_ripple * 0.5)
    glEnd()
    
    glColor3f(0.3, 0.5, 0.8)
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(33):
        angle = i * 2 * math.pi / 32
        inner_x = pond_radius * 0.6 * math.cos(angle)
        inner_y = pond_radius * 0.6 * math.sin(angle)
        outer_x = pond_radius * math.cos(angle)
        outer_y = pond_radius * math.sin(angle)
        
        glVertex3f(inner_x, inner_y, 0.2 + water_ripple * 0.5)
        glVertex3f(outer_x, outer_y, 0.2 + water_ripple * 0.3)
    glEnd()
    
    reflection_offset = math.sin(current_time * 3) * 0.05
    glColor3f(0.6, 0.7, 0.9)
    
    for i, (rx, ry, scale) in enumerate([(0.3, 0.2, 0.4), (-0.2, 0.4, 0.3), (0.1, -0.3, 0.35)]):
        reflection_radius = pond_radius * scale
        offset_time = current_time + i * 0.7
        ripple_x = rx * pond_radius + math.cos(offset_time) * 2
        ripple_y = ry * pond_radius + math.sin(offset_time * 1.2) * 2
        
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(ripple_x, ripple_y, 0.25 + reflection_offset)
        for j in range(17):
            angle = j * 2 * math.pi / 16
            px = ripple_x + reflection_radius * math.cos(angle)
            py = ripple_y + reflection_radius * math.sin(angle)
            glVertex3f(px, py, 0.25 + reflection_offset)
        glEnd()
    
    for ripple_index in range(3):
        ripple_time = current_time + ripple_index * 2
        ripple_radius = (ripple_time % 6) * pond_radius / 6
        ripple_alpha = 1.0 - (ripple_time % 6) / 6
        
        if ripple_radius < pond_radius:
            glColor3f(0.8 * ripple_alpha, 0.9 * ripple_alpha, 1.0 * ripple_alpha)
            glLineWidth(2)
            glBegin(GL_LINE_LOOP)
            for i in range(24):
                angle = i * 2 * math.pi / 24
                px = ripple_radius * math.cos(angle)
                py = ripple_radius * math.sin(angle)
                glVertex3f(px, py, 0.3)
            glEnd()
    
    lily_positions = [(0.4, 0.3), (-0.5, 0.2), (0.2, -0.6), (-0.3, -0.4)]
    for i, (lx, ly) in enumerate(lily_positions):
        lily_x = lx * pond_radius * 0.8
        lily_y = ly * pond_radius * 0.8
        lily_bob = math.sin(current_time + i) * 0.2
        
        if math.sqrt(lily_x**2 + lily_y**2) < pond_radius * 0.9:
            glPushMatrix()
            glTranslatef(lily_x, lily_y, 0.3 + lily_bob)
            
            glColor3f(0.2, 0.6, 0.3)
            glBegin(GL_TRIANGLE_FAN)
            glVertex3f(0, 0, 0)
            lily_size = 3 + math.sin(current_time + i) * 0.5
            for j in range(13):
                angle = j * 2 * math.pi / 12
                px = lily_size * math.cos(angle)
                py = lily_size * math.sin(angle)
                glVertex3f(px, py, 0)
            glEnd()
            
            if i % 2 == 0:
                glTranslatef(0, 0, 1)
                glColor3f(1.0, 0.8, 0.9)
                gluSphere(gluNewQuadric(), 1, 6, 4)
            
            glPopMatrix()
    
    glPopMatrix()

def draw_animal(animal):
    if animal["state"] == "dead" and time.time() - animal["death_time"] > 3:
        return  # Don't draw if dead for more than 3 seconds
    
    x, y = animal["x"], animal["y"]
    animal_type = animal["type"]
    config = ANIMAL_TYPES[animal_type]
    size = config["size"]
    
    glPushMatrix()
    glTranslatef(x, y, 0)

    # Ground shadow (simple blob shadow)
    glColor4f(0.0, 0.0, 0.0, 0.25)
    glPushMatrix()
    glTranslatef(0, 0, 0.1)
    glScalef(1.0, 1.0, 0.1)
    # Flattened ellipse varies by species size
    shadow_r = ANIMAL_TYPES[animal_type]["size"] * 0.7
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    for i in range(32):
        ang = i * (2 * math.pi / 31)
        glVertex3f(math.cos(ang) * shadow_r, math.sin(ang) * shadow_r * 0.7, 0)
    glEnd()
    glPopMatrix()
    
    if animal["state"] == "dead":
        # Draw dead animal lying on ground
        glRotatef(90, 0, 1, 0)  # Rotate to lie on side
        glTranslatef(0, 0, -size * 0.3)
        alpha = max(0, 1.0 - (time.time() - animal["death_time"]) / 3.0)
        glColor3f(config["color"][0] * alpha, config["color"][1] * alpha, config["color"][2] * alpha)
    else:
        # Rotate animal to face movement direction
        if animal["target_x"] is not None and animal["target_y"] is not None:
            dx = animal["target_x"] - x
            dy = animal["target_y"] - y
            if abs(dx) > 0.1 or abs(dy) > 0.1:
                angle = math.degrees(math.atan2(dx, dy))
                glRotatef(angle, 0, 0, 1)
        # Apply extra spin for showcase
        if animal.get("spinning") or animal.get("spin_angle", 0.0) != 0.0:
            glRotatef(animal.get("spin_angle", 0.0), 0, 0, 1)
        
        # Apply damage color tint
        damage_ratio = 1.0 - (animal["health"] / animal["max_health"])
        red_tint = damage_ratio * 0.3
        glColor3f(config["color"][0] + red_tint, config["color"][1], config["color"][2])
    
    # Draw body based on animal type
    if animal_type == "bear":
        draw_bear_body(size)
    elif animal_type == "deer":
        draw_deer_body(size, animal["state"])
    elif animal_type == "fox":
        draw_fox_body(size)
    
    glPopMatrix()

def draw_bear_body(size):
    config = ANIMAL_TYPES["bear"]
    
    # Main body - large and bulky with rich brown color
    glColor3f(*config["color"])
    glPushMatrix()
    glTranslatef(0, 0, size * 0.6)
    glScalef(1.3, 0.9, 0.75)
    gluSphere(gluNewQuadric(), size * 0.8, 16, 12)
    glPopMatrix()

    # Shoulder hump - distinctive bear silhouette
    glColor3f(config["color"][0] * 0.95, config["color"][1] * 0.95, config["color"][2] * 0.95)
    glPushMatrix()
    glTranslatef(0, size * 0.25, size * 1.0)
    glScalef(1.1, 0.8, 0.6)
    gluSphere(gluNewQuadric(), size * 0.45, 12, 10)
    glPopMatrix()

    # Rear haunch - fuller back
    glColor3f(config["color"][0] * 0.95, config["color"][1] * 0.85, config["color"][2] * 0.85)
    glPushMatrix()
    glTranslatef(0, -size * 0.35, size * 0.8)
    glScalef(1.0, 0.9, 0.7)
    gluSphere(gluNewQuadric(), size * 0.55, 12, 10)
    glPopMatrix()
    
    # Secondary body texture - lighter brown patches
    glColor3f(*config["secondary_color"])
    for patch_pos in [(-size * 0.3, size * 0.2, size * 0.7), 
                      (size * 0.4, -size * 0.1, size * 0.5),
                      (-size * 0.2, -size * 0.3, size * 0.8)]:
        glPushMatrix()
        glTranslatef(*patch_pos)
        glScalef(0.3, 0.3, 0.3)
        gluSphere(gluNewQuadric(), size * 0.3, 8, 6)
        glPopMatrix()
    
    # Head - darker brown
    glColor3f(config["color"][0] * 0.8, config["color"][1] * 0.8, config["color"][2] * 0.8)
    glPushMatrix()
    glTranslatef(0, size * 0.7, size * 0.8)
    gluSphere(gluNewQuadric(), size * 0.4, 12, 10)
    glPopMatrix()
    
    # Neck connection
    glColor3f(config["color"][0] * 0.9, config["color"][1] * 0.7, config["color"][2] * 0.7)
    glPushMatrix()
    glTranslatef(0, size * 0.55, size * 0.75)
    glScalef(0.6, 1.0, 0.8)
    gluSphere(gluNewQuadric(), size * 0.2, 8, 6)
    glPopMatrix()

    # Snout - lighter color
    glColor3f(*config["accent_color"])
    glPushMatrix()
    glTranslatef(0, size * 1.0, size * 0.7)
    glScalef(0.6, 1.2, 0.8)
    gluSphere(gluNewQuadric(), size * 0.15, 8, 6)
    glPopMatrix()

    # Nose tip (black)
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(0, size * 1.05, size * 0.68)
    gluSphere(gluNewQuadric(), size * 0.03, 6, 4)
    glPopMatrix()
    
    # Ears - main color
    glColor3f(*config["color"])
    for ear_x in [-size * 0.2, size * 0.2]:
        glPushMatrix()
        glTranslatef(ear_x, size * 0.8, size * 1.1)
        gluSphere(gluNewQuadric(), size * 0.12, 8, 6)
        glPopMatrix()
    
    # Eyes - much more visible with bright white patches
    for eye_x in [-size * 0.1, size * 0.1]:
        # Large white eye patch for contrast
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        glTranslatef(eye_x, size * 0.88, size * 0.88)
        gluSphere(gluNewQuadric(), size * 0.08, 12, 10)
        glPopMatrix()
        
        # Pure black pupil - very visible
        glColor3f(0.0, 0.0, 0.0)
        glPushMatrix()
        glTranslatef(eye_x, size * 0.90, size * 0.90)
        gluSphere(gluNewQuadric(), size * 0.05, 10, 8)
        glPopMatrix()
        
        # Large bright highlight for visibility
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        glTranslatef(eye_x + size * 0.02, size * 0.92, size * 0.92)
        gluSphere(gluNewQuadric(), size * 0.02, 8, 6)
        glPopMatrix()
    
    # Claws - cream colored
    glColor3f(*config["accent_color"])
    leg_positions = [(-size * 0.4, size * 0.3), (size * 0.4, size * 0.3), 
                    (-size * 0.4, -size * 0.3), (size * 0.4, -size * 0.3)]
    
    for leg_pos in leg_positions:
        # Leg - main color
        glColor3f(*config["color"])
        glPushMatrix()
        glTranslatef(leg_pos[0], leg_pos[1], size * 0.2)
        gluCylinder(gluNewQuadric(), size * 0.15, size * 0.12, size * 0.4, 10, 6)
        glPopMatrix()
        
        # Paw - secondary color
        glColor3f(*config["secondary_color"])
        glPushMatrix()
        glTranslatef(leg_pos[0], leg_pos[1], size * 0.05)
        gluSphere(gluNewQuadric(), size * 0.12, 8, 6)
        glPopMatrix()
        
        # Claws - accent color
        glColor3f(*config["accent_color"])
        for claw_angle in [0, 45, 90, 135]:
            claw_x = leg_pos[0] + math.cos(math.radians(claw_angle)) * size * 0.1
            claw_y = leg_pos[1] + math.sin(math.radians(claw_angle)) * size * 0.1
            glPushMatrix()
            glTranslatef(claw_x, claw_y, size * 0.02)
            glRotatef(claw_angle, 0, 0, 1)
            gluCylinder(gluNewQuadric(), size * 0.02, size * 0.01, size * 0.08, 4, 2)
            glPopMatrix()

    # Short tail stub
    glColor3f(*config["color"])
    glPushMatrix()
    glTranslatef(0, -size * 0.9, size * 0.8)
    gluSphere(gluNewQuadric(), size * 0.10, 8, 6)
    glPopMatrix()

def draw_deer_body(size, state):
    # Body (elegant, slender)
    glPushMatrix()
    glTranslatef(0, 0, 18)
    if state == "attacking":
        glColor3f(0.8, 0.6, 0.3)  # Startled coloring
    else:
        glColor3f(0.6, 0.4, 0.2)  # Brown deer
    glScalef(0.8, 1.5, 1.0)
    gluSphere(gluNewQuadric(), 10, 10, 8)
    glPopMatrix()
    
    # Head
    glPushMatrix()
    glTranslatef(0, 12, 25)
    glColor3f(0.65, 0.45, 0.25)
    glScalef(0.8, 1.2, 0.9)
    gluSphere(gluNewQuadric(), 5, 8, 6)
    glPopMatrix()
    
    # Long snout
    glPushMatrix()
    glTranslatef(0, 18, 25)
    glColor3f(0.5, 0.35, 0.2)
    glScalef(0.6, 1.8, 0.6)
    gluSphere(gluNewQuadric(), 2.5, 6, 4)
    glPopMatrix()
    
    # Large ears
    for ear_x in [-3, 3]:
        glPushMatrix()
        glTranslatef(ear_x, 10, 30)
        glColor3f(0.55, 0.4, 0.2)
        glScalef(0.5, 0.3, 1.5)
        gluSphere(gluNewQuadric(), 4, 6, 8)
        glPopMatrix()
    
    # Eyes - visible black eyes on the face
    for eye_x in [-2, 2]:
        # Eye white/light background for contrast
        glColor3f(0.9, 0.9, 0.85)
        glPushMatrix()
        glTranslatef(eye_x, 15, 27)
        gluSphere(gluNewQuadric(), 1.2, 8, 6)
        glPopMatrix()
        
        # Black pupil - visible and prominent
        glColor3f(0.0, 0.0, 0.0)
        glPushMatrix()
        glTranslatef(eye_x, 15.5, 27.2)
        gluSphere(gluNewQuadric(), 0.8, 8, 6)
        glPopMatrix()
        
        # Small white highlight
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        glTranslatef(eye_x + 0.3, 15.7, 27.4)
        gluSphere(gluNewQuadric(), 0.3, 6, 4)
        glPopMatrix()
    
    # Antlers (if not attacking - deer run away)
    if state != "attacking":
        glColor3f(0.8, 0.7, 0.5)
        for antler_x in [-2, 2]:
            glPushMatrix()
            glTranslatef(antler_x, 8, 32)
            glRotatef(antler_x * 15, 0, 1, 0)
            gluCylinder(gluNewQuadric(), 0.8, 0.3, 12, 6, 2)
            # Antler branches
            for branch_z in [4, 8]:
                glPushMatrix()
                glTranslatef(0, 0, branch_z)
                glRotatef(45, 1, 0, 0)
                gluCylinder(gluNewQuadric(), 0.4, 0.1, 6, 4, 1)
                glPopMatrix()
            glPopMatrix()
    
    # Thin legs
    glColor3f(0.5, 0.3, 0.15)
    for leg_pos in [(-4, -6, 0), (4, -6, 0), (-4, 6, 0), (4, 6, 0)]:
        glPushMatrix()
        glTranslatef(leg_pos[0], leg_pos[1], leg_pos[2])
        gluCylinder(gluNewQuadric(), 1.5, 1, 16, 6, 2)
        glPopMatrix()
    
    # Small tail
    glPushMatrix()
    glTranslatef(0, -10, 18)
    glColor3f(0.7, 0.5, 0.3)
    gluSphere(gluNewQuadric(), 2, 6, 4)
    glPopMatrix()

def draw_fox_body(size):
    config = ANIMAL_TYPES["fox"]
    
    # Main body - small and agile with bright orange
    glColor3f(*config["color"])
    glPushMatrix()
    glTranslatef(0, 0, size * 0.4)
    glScalef(0.8, 1.0, 0.5)
    gluSphere(gluNewQuadric(), size * 0.6, 12, 8)
    glPopMatrix()
    
    # White chest marking
    glColor3f(*config["accent_color"])
    glPushMatrix()
    glTranslatef(0, size * 0.3, size * 0.35)
    glScalef(0.6, 0.4, 0.8)
    gluSphere(gluNewQuadric(), size * 0.3, 8, 6)
    glPopMatrix()
    
    # Head - pointed snout with gradient coloring
    glColor3f(*config["color"])
    glPushMatrix()
    glTranslatef(0, size * 0.5, size * 0.5)
    glScalef(0.7, 1.2, 0.8)
    gluSphere(gluNewQuadric(), size * 0.25, 10, 8)
    glPopMatrix()
    
    # White snout tip
    glColor3f(*config["accent_color"])
    glPushMatrix()
    glTranslatef(0, size * 0.7, size * 0.45)
    glScalef(0.5, 0.8, 0.6)
    gluSphere(gluNewQuadric(), size * 0.12, 6, 4)
    glPopMatrix()
    
    # Ears - large, pointed, and distinctive
    glColor3f(*config["color"])
    for ear_x in [-size * 0.15, size * 0.15]:
        # Outer ear - orange
        glPushMatrix()
        glTranslatef(ear_x, size * 0.6, size * 0.7)
        glRotatef(15, 1, 0, 0)
        glScalef(0.8, 0.6, 2.0)
        gluSphere(gluNewQuadric(), size * 0.08, 6, 4)
        glPopMatrix()
        
        # Inner ear - secondary color (lighter orange)
        glColor3f(*config["secondary_color"])
        glPushMatrix()
        glTranslatef(ear_x, size * 0.62, size * 0.72)
        glRotatef(15, 1, 0, 0)
        glScalef(0.5, 0.4, 1.5)
        gluSphere(gluNewQuadric(), size * 0.06, 4, 3)
        glPopMatrix()
        glColor3f(*config["color"])  # Reset color
    
    # Eyes - bright blue and alert (two eyes with highlights)
    for eye_x in [-size * 0.09, size * 0.09]:
        # Iris
        glColor3f(*config["eye_color"])
        glPushMatrix()
        glTranslatef(eye_x, size * 0.66, size * 0.60)
        gluSphere(gluNewQuadric(), size * 0.035, 8, 6)
        glPopMatrix()
        # Pupil (black)
        glColor3f(0.0, 0.0, 0.0)
        glPushMatrix()
        glTranslatef(eye_x, size * 0.67, size * 0.62)
        gluSphere(gluNewQuadric(), size * 0.015, 6, 4)
        glPopMatrix()
        # Specular highlight (white dot)
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        glTranslatef(eye_x + size * 0.01, size * 0.68, size * 0.63)
        gluSphere(gluNewQuadric(), size * 0.008, 4, 3)
        glPopMatrix()
    
    # Nose - black
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(0, size * 0.75, size * 0.48)
    gluSphere(gluNewQuadric(), size * 0.02, 4, 3)
    glPopMatrix()
    
    # Tail - extra fluffy and vibrant with bright colors
    glColor3f(1.0, 0.5, 0.0)  # More vibrant orange than body
    glPushMatrix()
    glTranslatef(0, -size * 0.65, size * 0.35)
    glRotatef(30, 1, 0, 0)

    # Multiple overlapping segments for maximum fluff
    tail_colors = [(1.0, 0.5, 0.0), (1.0, 0.6, 0.1), (1.0, 0.4, 0.0)]
    for segment in range(8):
        color_idx = segment % len(tail_colors)
        glColor3f(*tail_colors[color_idx])
        glPushMatrix()
        glTranslatef(0, 0, segment * size * 0.10)
        scale = 1.2 - segment * 0.08
        glScalef(scale, scale, 1.5)
        gluSphere(gluNewQuadric(), size * (0.18 - segment * 0.008), 12, 10)
        glPopMatrix()

    # Pure white tail tip - extra fluffy
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslatef(0, 0, size * 0.58)
    gluSphere(gluNewQuadric(), size * 0.15, 12, 10)
    glPopMatrix()
    glPopMatrix()
    
    # Mouth - realistic fox snout with small mouth opening
    glColor3f(0.0, 0.0, 0.0)  # Black mouth opening
    glPushMatrix()
    glTranslatef(0, size * 0.75, size * 0.46)
    glScalef(0.3, 0.1, 0.2)
    gluSphere(gluNewQuadric(), size * 0.03, 6, 4)
    glPopMatrix()
    
    # Small teeth/fangs for realism
    glColor3f(1.0, 1.0, 1.0)
    for fang_x in [-size * 0.015, size * 0.015]:
        glPushMatrix()
        glTranslatef(fang_x, size * 0.74, size * 0.47)
        glRotatef(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), size * 0.005, size * 0.002, size * 0.02, 4, 2)
        glPopMatrix()
    
    # Legs - delicate and quick
    leg_positions = [(-size * 0.2, size * 0.1), (size * 0.2, size * 0.1), 
                    (-size * 0.2, -size * 0.1), (size * 0.2, -size * 0.1)]
    
    for leg_pos in leg_positions:
        # Upper leg - orange
        glColor3f(*config["color"])
        glPushMatrix()
        glTranslatef(leg_pos[0], leg_pos[1], size * 0.15)
        gluCylinder(gluNewQuadric(), size * 0.08, size * 0.06, size * 0.15, 8, 4)
        glPopMatrix()
        
        # Lower leg - secondary color
        glColor3f(*config["secondary_color"])
        glPushMatrix()
        glTranslatef(leg_pos[0], leg_pos[1], size * 0.05)
        gluCylinder(gluNewQuadric(), size * 0.06, size * 0.05, size * 0.15, 6, 4)
        glPopMatrix()
        
        # Paw - white
        glColor3f(*config["accent_color"])
        glPushMatrix()
        glTranslatef(leg_pos[0], leg_pos[1], size * 0.02)
        gluSphere(gluNewQuadric(), size * 0.06, 6, 4)
        glPopMatrix()
    
    # Facial markings - white stripes
    glColor3f(*config["accent_color"])
    for stripe_y in [size * 0.55, size * 0.6]:
        for stripe_x in [-size * 0.05, size * 0.05]:
            glPushMatrix()
            glTranslatef(stripe_x, stripe_y, size * 0.52)
            glScalef(0.3, 0.8, 0.3)
            gluSphere(gluNewQuadric(), size * 0.04, 4, 3)
            glPopMatrix()

def draw_bullet(bullet):
    glPushMatrix()
    glTranslatef(bullet["x"], bullet["y"], bullet["z"])
    # Use the bullet's stored color instead of default yellow
    glColor3f(*bullet["color"])
    gluSphere(gluNewQuadric(), 1.5, 8, 6)  # Slightly larger and more detailed bullets
    glPopMatrix()

def spawn_chunk(ci):
    y0 = ci * CHUNK_LEN
    y1 = (ci + 1) * CHUNK_LEN
    minx, maxx = -GRID_HALF_X + 20, GRID_HALF_X - 20

    entry = {"trees":[], "stones":[], "traps":[], "foods":[], "ammos":[], "waters":[], "animals":[]}

    for _ in range(rand.randint(*TREE_COUNT_PER_CHUNK)):
        tree_x = rand.randint(minx, maxx)
        tree_y = rand.randint(y0+10, y1-10)
        tree_type = rand.choice([0, 1])  
        entry["trees"].append((tree_x, tree_y, tree_type))

    for _ in range(rand.randint(*STONE_COUNT_PER_CHUNK)):
        stone_size = rand.randint(15, 35)  
        is_small = stone_size < 25  
        entry["stones"].append({
            "x": rand.randint(minx, maxx), 
            "y": rand.randint(y0+10, y1-10), 
            "size": stone_size,
            "height": 12 if is_small else 40, 
            "is_small": is_small
        })

    for _ in range(rand.randint(*TRAP_COUNT_PER_CHUNK)):
        entry["traps"].append({"x": rand.randint(minx, maxx), "y": rand.randint(y0+10, y1-10), "w": 26, "l": 26})

    for _ in range(rand.randint(*FOOD_COUNT_PER_CHUNK)):
        entry["foods"].append({"x": rand.randint(minx, maxx), "y": rand.randint(y0+10, y1-10)})

    for _ in range(rand.randint(*AMMO_COUNT_PER_CHUNK)):
        entry["ammos"].append({"x": rand.randint(minx, maxx), "y": rand.randint(y0+10, y1-10), "amount": rand.randint(10, 20)})

    for _ in range(rand.randint(*WATER_COUNT_PER_CHUNK)):
        entry["waters"].append({"x": rand.randint(minx, maxx), "y": rand.randint(y0+10, y1-10), "w": rand.randint(40, 70), "l": rand.randint(40, 70)})

    # Spawn animals
    for _ in range(rand.randint(*ANIMAL_COUNT_PER_CHUNK)):
        animal_type = rand.choice(["bear", "deer", "fox"])
        config = ANIMAL_TYPES[animal_type]
        animal = {
            "type": animal_type,
            "x": rand.randint(minx, maxx),
            "y": rand.randint(y0+10, y1-10),
            "health": config["health"],
            "max_health": config["health"],
            "state": "wandering",  # wandering, chasing, attacking, dead
            "target_x": None,
            "target_y": None,
            "last_attack_time": 0,
            "death_time": 0,
            "wander_target_x": None,
            "wander_target_y": None,
            "wander_change_time": time.time() + rand.uniform(2, 5),
            # continuous rotation angle
            "spin_angle": 0.0
        }
        entry["animals"].append(animal)

    chunks[ci] = entry

def ensure_chunks():
    global last_generated_chunk
    cidx = int(camera["y"] // CHUNK_LEN)
   
    for ci in range(cidx, cidx + VISIBLE_CHUNKS_AHEAD + 1):
        if ci not in chunks:
            spawn_chunk(ci)
            last_generated_chunk = max(last_generated_chunk, ci)
    
    for k in list(chunks.keys()):
        if k < cidx - VISIBLE_CHUNKS_BEHIND:
            del chunks[k]

def collect_active_lists():
    
    foods.clear(); ammos.clear(); traps.clear(); stones.clear(); waters.clear(); animals.clear()
    cidx = int(camera["y"] // CHUNK_LEN)
    for ci in range(cidx - 1, cidx + VISIBLE_CHUNKS_AHEAD + 1):
        if ci in chunks:
            ch = chunks[ci]
            for f in ch["foods"]:   foods.append(f)
            for a in ch["ammos"]:   ammos.append(a)
            for r in ch["traps"]:   traps.append(r)
            for s in ch["stones"]:  stones.append(s)
            for w in ch["waters"]:  waters.append(w)
            for an in ch["animals"]: animals.append(an)


def restart_game():
    """Reset player health and position when game is restarted"""
    global player_health, player_pos, last_damage_time, player_jumping, jump_velocity, in_water
    global is_walking, walking_animation_time, current_weapon
    global cheat_mode_active, cheat_mode_used, cheat_activation_time
    global game_start_time, current_score, game_over
    
    # Reset health system - start with 100 health for better gameplay
    player_health = 100.0
    last_damage_time = 0.0
    
    # Reset player position
    player_pos = {"x": 0.0, "y": 50.0, "z": 0.0}
    player_jumping = False
    jump_velocity = 0.0
    in_water = False
    
    # Reset walking animation
    is_walking = False
    walking_animation_time = 0.0
    
    # Reset weapon to default
    current_weapon = "left"
    
    # IMPORTANT: Reset superpower system - making it available again!
    cheat_mode_active = False
    cheat_mode_used = False  # This makes the superpower available again
    cheat_activation_time = 0.0
    
    # Reset scoring system
    game_start_time = time.time()
    current_score = 0.0
    game_over = False
    
    print("Game restarted! Health restored to 100. Weapon reset to Left (Rifle).")
    print("✨ SUPER POWER is now AVAILABLE! Press 'G' to activate 10 seconds of maximum speed! ✨")

def activate_super_power():
    """Activate the one-time super power cheat mode"""
    global cheat_mode_active, cheat_mode_used, cheat_activation_time
    
    if game_over:
        print("Cannot activate super power when game is over!")
        return  # Don't activate if game is over
    
    if cheat_mode_used:
        print("❌ Super power already used this game! Only one use per game allowed.")
        print("💡 Tip: Restart the game (press 'R' or Backspace) to get the super power back!")
        return
    
    if cheat_mode_active:
        print("⚡ Super power already active!")
        return
    
    # Activate super power
    cheat_mode_active = True
    cheat_mode_used = True
    cheat_activation_time = time.time()
    print("🚀 SUPER POWER ACTIVATED! 🚀")
    print("⚡ 10 seconds of maximum speed with no obstacles! ⚡")
    print("🏃‍♂️ Move with WASD - you can pass through everything!")
    print("You can now move through trees, stones, and animals at maximum speed!")

def show_super_power_info():
    """Show current super power status and instructions"""
    global cheat_mode_active, cheat_mode_used, cheat_activation_time, cheat_mode_duration
    
    print("=== SUPER POWER STATUS ===")
    if cheat_mode_active:
        remaining_time = cheat_mode_duration - (time.time() - cheat_activation_time)
        if remaining_time > 0:
            print(f"⚡ SUPER POWER ACTIVE! {remaining_time:.1f} seconds remaining")
            print("🏃‍♂️ You can move through all obstacles at maximum speed!")
        else:
            print("⏰ Super power expired")
    elif cheat_mode_used:
        print("❌ Super power already used this game")
        print("💡 Restart the game (press 'R' or Backspace) to get it back!")
    else:
        print("✨ Super power AVAILABLE! Press 'G' to activate!")
        print("⚡ Gives you 10 seconds of maximum speed with no obstacle collisions")
    
    print("📋 Controls:")
    print("  G - Activate super power (once per game)")
    print("  R - Restart game (resets super power)")
    print("  Backspace - Restart viewer")
    print("  I - Show this info")
    print("=========================")

def keyboardListener(key, x, y):
    k = key.lower()
    
 
    if k == b'p':  
        global game_paused
        game_paused = not game_paused
        print(f"Viewer {'PAUSED' if game_paused else 'RESUMED'}")
        return
    elif k == b'\x08':  
        restart_viewer()
        return
    elif k == b'\x1b':  
        print("Viewer quit")
        import sys
        sys.exit()
        return
    elif k == b'r':  # Restart game (especially when health is 0)
        restart_game()
        return
    
    if game_paused:
        return
    
    # Player movement controls
    if k == b'w':
        move_player("forward")
    elif k == b's':
        move_player("backward")
    elif k == b'a':
        move_player("left")
    elif k == b'd':
        move_player("right")
    elif k == b' ':  # Jump
        jump_player()
    elif k == b'q':  # Switch weapon
        switch_weapon()
    elif k == b'f':  # Toggle cheat mode
        global cheat_mode
        cheat_mode = not cheat_mode
        print(f"Cheat mode {'ENABLED' if cheat_mode else 'DISABLED'} - {'Both weapons fire simultaneously' if cheat_mode else 'Normal weapon switching'}")
    elif k == b'g':  # Activate super power cheat mode (once per game)
        activate_super_power()
    elif k == b'i':  # Show super power information
        show_super_power_info()
    elif k == b'x':  # Camera down (keep for camera control)
        camera["z"] -= 13.0
    elif k == b'c':  
        camera["fpv"] = not camera["fpv"]
        print(f"Camera: {'First Person' if camera['fpv'] else 'Third Person'}")
 
    # Update camera to follow player
    camera["x"] = player_pos["x"]
    camera["y"] = player_pos["y"] - 30  # Camera behind player
    
    # Clamp camera position
    camera["x"] = clamp(camera["x"], -GRID_HALF_X+5, GRID_HALF_X-5)
    camera["z"] = clamp(camera["z"], 5.0, 200.0)

def specialKeyListener(key, x, y):
    global camera_yaw, camera_pitch
    
    if game_paused:
        return
        
    
    if key == GLUT_KEY_LEFT:
        camera_yaw -= CAMERA_ROTATION_SPEED
        if camera_yaw < 0:
            camera_yaw += 360
        print(f"Camera Yaw: {camera_yaw:.1f}°")
        
    elif key == GLUT_KEY_RIGHT:
        camera_yaw += CAMERA_ROTATION_SPEED
        if camera_yaw >= 360:
            camera_yaw -= 360
        print(f"Camera Yaw: {camera_yaw:.1f}°")
        
    elif key == GLUT_KEY_UP:
        camera_pitch += CAMERA_ROTATION_SPEED
        camera_pitch = min(camera_pitch, MAX_PITCH)
        print(f"Camera Pitch: {camera_pitch:.1f}°")
        
    elif key == GLUT_KEY_DOWN:
        camera_pitch -= CAMERA_ROTATION_SPEED
        camera_pitch = max(camera_pitch, MIN_PITCH)
        print(f"Camera Pitch: {camera_pitch:.1f}°")

def mouseListener(button, state, x, y):
    """Handle mouse clicks for weapon firing"""
    if game_paused or player_health <= 0:
        return
        
    # Only fire on mouse button press (down), not release (up)
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            # Left mouse button fires left weapon (rifle)
            if cheat_mode:
                shoot_both_weapons()  # Fire both weapons in cheat mode
            else:
                shoot_bullet("left")
        elif button == GLUT_RIGHT_BUTTON:
            # Right mouse button fires right weapon (pistol)
            if cheat_mode:
                shoot_both_weapons()  # Fire both weapons in cheat mode
            else:
                shoot_bullet("right")

def shoot_bullet(weapon="left"):
    """Shoot bullet from specified weapon (left rifle or right pistol)"""
    global player
    current_time = time.time()
    
    # Check weapon-specific ammo
    if weapon == "left":
        if player["rifle_ammo"] <= 0:
            print("No rifle ammo! Press R near ammo boxes to reload.")
            return
        current_ammo = player["rifle_ammo"]
    else:
        if player["pistol_ammo"] <= 0:
            print("No pistol ammo! Press R near ammo boxes to reload.")
            return
        current_ammo = player["pistol_ammo"]
    
    # Rate limiting (except in cheat mode)
    if not cheat_mode and current_time - player["last_shot_time"] < 0.3:
        return
    
    # Consume ammo
    if weapon == "left":
        player["rifle_ammo"] -= 1
    else:
        player["pistol_ammo"] -= 1
        
    player["last_shot_time"] = current_time
    
    # Calculate bullet direction based on camera orientation
    yaw_rad = math.radians(camera_yaw)
    pitch_rad = math.radians(camera_pitch)
    
    # Get player position for bullet spawn location
    spawn_x = player_pos["x"]
    spawn_y = player_pos["y"]
    spawn_z = player_pos["z"] + 15  # Spawn at chest height
    
    # Offset bullet spawn based on weapon (left or right)
    if weapon == "left":
        # Rifle (left weapon) - blue bullets
        offset_x = -4 * math.cos(yaw_rad)  # Left side offset
        offset_y = 4 * math.sin(yaw_rad)
        bullet_color = (0.2, 0.5, 1.0)  # Blue bullets for rifle
        bullet_speed = 300  # Much faster bullets for straight trajectory
        remaining_ammo = player["rifle_ammo"]
        print(f"Left weapon (Rifle) fired! Rifle ammo remaining: {remaining_ammo}")
    else:
        # Pistol (right weapon) - red bullets  
        offset_x = 4 * math.cos(yaw_rad)   # Right side offset
        offset_y = -4 * math.sin(yaw_rad)
        bullet_color = (1.0, 0.2, 0.2)  # Red bullets for pistol
        bullet_speed = 280  # High speed bullets for straight trajectory
        remaining_ammo = player["pistol_ammo"]
        print(f"Right weapon (Pistol) fired! Pistol ammo remaining: {remaining_ammo}")
    
    bullet = {
        "x": spawn_x + offset_x,
        "y": spawn_y + offset_y,
        "z": spawn_z,
        "vel_x": bullet_speed * math.cos(pitch_rad) * math.sin(yaw_rad),
        "vel_y": bullet_speed * math.cos(pitch_rad) * math.cos(yaw_rad),
        "vel_z": bullet_speed * math.sin(pitch_rad),
        "life": 2.0,  # Shorter life for high-speed bullets
        "color": bullet_color,  # Store bullet color
        "weapon": weapon  # Track which weapon fired this bullet
    }
    bullets.append(bullet)

def shoot_both_weapons():
    """Cheat mode: Fire both weapons simultaneously"""
    shoot_bullet("left")   # Fire rifle
    shoot_bullet("right")  # Fire pistol

def collect_nearby_ammo():
    global player, ammos
    collected = 0
    
    for i in range(len(ammos) - 1, -1, -1):  # Iterate backwards for safe removal
        ammo_box = ammos[i]
        # Use player position instead of camera position
        dist = math.sqrt((ammo_box["x"] - player_pos["x"])**2 + (ammo_box["y"] - player_pos["y"])**2)
        if dist < 25:  # Collection radius
            # Increase both weapon ammo types
            player["rifle_ammo"] += ammo_box["amount"]
            player["pistol_ammo"] += ammo_box["amount"]
            
            # Store ammo_box data before removal
            ammo_x, ammo_y = ammo_box["x"], ammo_box["y"]
            
            # Remove from global ammos list
            ammos.pop(i)
            
            # Remove from chunks too
            for chunk in chunks.values():
                for j in range(len(chunk["ammos"]) - 1, -1, -1):
                    chunk_ammo = chunk["ammos"][j]
                    if chunk_ammo["x"] == ammo_x and chunk_ammo["y"] == ammo_y:
                        chunk["ammos"].pop(j)
                        break
            
            collected += ammo_box["amount"]
    
    if collected > 0:
        print(f"Collected {collected} ammo for each weapon! Rifle: {player['rifle_ammo']}, Pistol: {player['pistol_ammo']}")
    else:
        print("No ammo nearby!")

# Auto-rotation enabled: helper removed

def update_bullets(dt):
    for bullet in bullets[:]:  # Copy list to avoid modification during iteration
        # Update position - bullets travel in straight lines at high speed
        bullet["x"] += bullet["vel_x"] * dt
        bullet["y"] += bullet["vel_y"] * dt
        bullet["z"] += bullet["vel_z"] * dt
        
        # No gravity applied - bullets travel straight
        
        # Remove if expired or too far from player
        bullet["life"] -= dt
        player_dist = math.sqrt((bullet["x"] - player_pos["x"])**2 + (bullet["y"] - player_pos["y"])**2)
        if bullet["life"] <= 0 or player_dist > 500:  # Remove bullets that go too far
            bullets.remove(bullet)
            continue
        
        # Check collision with animals
        for animal in animals[:]:  # Copy list to avoid modification during iteration
            if animal["state"] == "dead":
                continue
                
            dist = math.sqrt((bullet["x"] - animal["x"])**2 + 
                           (bullet["y"] - animal["y"])**2 + 
                           (bullet["z"] - (ANIMAL_TYPES[animal["type"]]["size"] * 0.5))**2)
            
            if dist < ANIMAL_TYPES[animal["type"]]["size"] * 0.6:
                # Hit animal - reduce health instead of instant kill
                animal_type = animal["type"]
                weapon_used = bullet["weapon"]
                
                # Remove bullet
                bullets.remove(bullet)
                
                # Reduce animal health by 1
                animal["health"] -= 1
                print(f"Hit {animal_type} with {weapon_used}! Health remaining: {animal['health']}")
                
                # Check if animal is dead
                if animal["health"] <= 0:
                    # Animal is now dead
                    animal["state"] = "dead"
                    print(f"{animal_type.capitalize()} killed!")
                    
                    # Remove animal from main animals list
                    animals.remove(animal)
                    
                    # Remove animal from all chunks
                    for chunk in chunks.values():
                        if animal in chunk["animals"]:
                            chunk["animals"].remove(animal)
                
                print(f"Killed a {animal_type} with {weapon_used} weapon! Animal vanished.")
                break

def update_animals(dt):
    current_time = time.time()
    for animal in animals:
        if animal["state"] == "dead":
            continue

        config = ANIMAL_TYPES[animal["type"]]

        # Continuous auto-rotation
        animal["spin_angle"] = (animal.get("spin_angle", 0.0) + SPIN_SPEED * dt) % 360.0

        # Check distance to player
        player_dist = math.sqrt((animal["x"] - camera["x"])**2 + (animal["y"] - camera["y"])**2)

        # State machine
        if animal["state"] == "wandering":
            # Change to chasing if player is within detection radius
            if player_dist < config["detection_radius"]:
                animal["state"] = "chasing"
                animal["target_x"] = camera["x"]
                animal["target_y"] = camera["y"]
                print(f"A {animal['type']} spotted you!")
            else:
                # Random wandering
                if (animal["wander_target_x"] is None or current_time > animal["wander_change_time"]):
                    # Pick new wander target
                    angle = rand.uniform(0, 2 * math.pi)
                    distance = rand.uniform(20, 80)
                    animal["wander_target_x"] = animal["x"] + math.cos(angle) * distance
                    animal["wander_target_y"] = animal["y"] + math.sin(angle) * distance
                    animal["wander_change_time"] = current_time + rand.uniform(3, 8)

                # Move towards wander target
                if animal["wander_target_x"] is not None:
                    dx = animal["wander_target_x"] - animal["x"]
                    dy = animal["wander_target_y"] - animal["y"]
                    distance = math.sqrt(dx*dx + dy*dy)
                    if distance > 5:
                        move_speed = config["speed"] * 0.3  # Slow wandering
                        new_x = animal["x"] + (dx / distance) * move_speed * dt
                        new_y = animal["y"] + (dy / distance) * move_speed * dt
                        
                        # Apply collision detection
                        valid_x, valid_y = get_valid_animal_position(animal, new_x, new_y)
                        animal["x"], animal["y"] = valid_x, valid_y
                        
                        # Avoid obstacles
                        avoid_obstacles(animal, dt)

        elif animal["state"] == "chasing":
            # Update target to current player position
            animal["target_x"] = camera["x"]
            animal["target_y"] = camera["y"]
            # Move towards player
            dx = camera["x"] - animal["x"]
            dy = camera["y"] - animal["y"]
            distance = math.sqrt(dx*dx + dy*dy)
            if distance < config["attack_radius"]:
                animal["state"] = "attacking"
                animal["last_attack_time"] = current_time
            elif distance > config["detection_radius"] * 1.5:
                # Lost player, return to wandering
                animal["state"] = "wandering"
                animal["wander_change_time"] = current_time
            else:
                # Chase player
                if distance > 0:
                    new_x = animal["x"] + (dx / distance) * config["speed"] * dt
                    new_y = animal["y"] + (dy / distance) * config["speed"] * dt
                    
                    # Apply collision detection
                    valid_x, valid_y = get_valid_animal_position(animal, new_x, new_y)
                    animal["x"], animal["y"] = valid_x, valid_y
                    
                    # Avoid obstacles
                    avoid_obstacles(animal, dt)

        elif animal["state"] == "attacking":
            # Attack player if close enough and enough time has passed
            if (player_dist < config["attack_radius"] and current_time - animal["last_attack_time"] > 1.5):
                # Trigger attack effects and damage
                damage_amount = config["damage"]
                trigger_attack_effect(damage_amount)
                
                global player_health
                player_health -= damage_amount
                player_health = max(0, player_health)  # Don't go below 0
                animal["last_attack_time"] = current_time
                
                print(f"{animal['type']} attacked you! Health: {player_health}")
                if player_health <= 0:
                    print("Game Over! You died! Press 'R' to restart.")
                    return
            # Move back to chasing if too far
            if player_dist > config["attack_radius"] * 1.2:
                animal["state"] = "chasing"

def avoid_obstacles(animal, dt):
    # Simple obstacle avoidance - check for trees and stones
    config = ANIMAL_TYPES[animal["type"]]
    avoidance_radius = config["size"] + 10
    
    original_x, original_y = animal["x"], animal["y"]
    
    for chunk in chunks.values():
        # Avoid trees
        for tree_data in chunk["trees"]:
            if len(tree_data) >= 2:
                tree_x, tree_y = tree_data[0], tree_data[1]
                dist = math.sqrt((animal["x"] - tree_x)**2 + (animal["y"] - tree_y)**2)
                
                if dist < avoidance_radius:
                    # Push away from tree
                    if dist > 0:
                        push_x = (animal["x"] - tree_x) / dist
                        push_y = (animal["y"] - tree_y) / dist
                        new_x = animal["x"] + push_x * config["speed"] * dt * 0.5
                        new_y = animal["y"] + push_y * config["speed"] * dt * 0.5
                        
                        # Apply collision detection even for obstacle avoidance
                        valid_x, valid_y = get_valid_animal_position(animal, new_x, new_y)
                        animal["x"], animal["y"] = valid_x, valid_y
        
        # Avoid stones
        for stone in chunk["stones"]:
            stone_x, stone_y = stone["x"], stone["y"]
            dist = math.sqrt((animal["x"] - stone_x)**2 + (animal["y"] - stone_y)**2)
            
            if dist < avoidance_radius:
                # Push away from stone
                if dist > 0:
                    push_x = (animal["x"] - stone_x) / dist
                    push_y = (animal["y"] - stone_y) / dist
                    new_x = animal["x"] + push_x * config["speed"] * dt * 0.5
                    new_y = animal["y"] + push_y * config["speed"] * dt * 0.5
                    
                    # Apply collision detection even for obstacle avoidance
                    valid_x, valid_y = get_valid_animal_position(animal, new_x, new_y)
                    animal["x"], animal["y"] = valid_x, valid_y
    
    # Keep within grid bounds
    animal["x"] = clamp(animal["x"], -GRID_HALF_X + 20, GRID_HALF_X - 20)

def setupCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, ASPECT, 0.1, 5000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Apply screen shake effect
    apply_screen_shake()
    
    yaw_rad = math.radians(camera_yaw)
    pitch_rad = math.radians(camera_pitch)
    look_distance = 80.0
    
    if camera["fpv"]:
        # First Person View - camera at player's eye level
        eye_x = player_pos["x"]
        eye_y = player_pos["y"]
        eye_z = player_pos["z"] + 20.0  # Eye level height (head height for doubled size player)
        
        # Calculate where we're looking
        look_x = eye_x + look_distance * math.cos(pitch_rad) * math.sin(yaw_rad)
        look_y = eye_y + look_distance * math.cos(pitch_rad) * math.cos(yaw_rad)
        look_z = eye_z + look_distance * math.sin(pitch_rad)
        
        gluLookAt(eye_x, eye_y, eye_z,
                  look_x, look_y, look_z,
                  *Z_UP)
    else:
        # Third Person View - camera behind player
        eye_z = camera["z"]
        look_x = camera["x"] + look_distance * math.cos(pitch_rad) * math.sin(yaw_rad)
        look_y = camera["y"] + look_distance * math.cos(pitch_rad) * math.cos(yaw_rad)
        look_z = eye_z + look_distance * math.sin(pitch_rad)
        
        cam_distance = 120.0
        cam_height = 60.0
        cam_x = camera["x"] - cam_distance * math.cos(pitch_rad * 0.5) * math.sin(yaw_rad)
        cam_y = camera["y"] - cam_distance * math.cos(pitch_rad * 0.5) * math.cos(yaw_rad)
        cam_z = eye_z + cam_height + cam_distance * math.sin(pitch_rad * 0.3)
        gluLookAt(cam_x, cam_y, cam_z,camera["x"], camera["y"], eye_z,*Z_UP)

def draw_world():

    draw_floor_grid()
    
    # Only draw the player in third-person view
    if not camera["fpv"]:
        player = Player((player_pos["x"], player_pos["y"], player_pos["z"]))
        player.draw()
    
    cidx = int(camera["y"] // CHUNK_LEN)
    chunk_range = list(range(cidx - 1, cidx + VISIBLE_CHUNKS_AHEAD + 1))
    chunk_range.sort(key=lambda ci: abs((ci * CHUNK_LEN + CHUNK_LEN/2) - camera["y"]), reverse=True)
    

    for ci in chunk_range:
        if ci not in chunks: continue
        ch = chunks[ci]
        
        for w in ch["waters"]:
            draw_water(w)
        for t in ch["traps"]:
            draw_trap(t)
        for f in ch["foods"]:
            draw_food(f)
        for a in ch["ammos"]:
            draw_ammo(a)
    
    # Draw bullets
    for bullet in bullets:
        draw_bullet(bullet)
    
    # Draw animals
    for animal in animals:
        draw_animal(animal)
    
    all_occluding_objects = []
    for ci in chunk_range:
        if ci not in chunks: continue
        ch = chunks[ci]

        for tree_data in ch["trees"]:
            if len(tree_data) == 3:  
                x, y, tree_type = tree_data
            else:  
                x, y = tree_data
                tree_type = 0  
            distance = math.sqrt((x - camera["x"])**2 + (y - camera["y"])**2)
            all_occluding_objects.append((distance, 'tree', x, y, tree_type))
        
        for stone_data in ch["stones"]:
            x, y = stone_data["x"], stone_data["y"]
            distance = math.sqrt((x - camera["x"])**2 + (y - camera["y"])**2)
            all_occluding_objects.append((distance, 'stone', stone_data))
    
    all_occluding_objects.sort(key=lambda obj: obj[0], reverse=True)
 
    for obj_data in all_occluding_objects:
        if obj_data[1] == 'tree':
            distance, obj_type, x, y, tree_type = obj_data
            draw_tree(x, y, tree_type)
        elif obj_data[1] == 'stone':
            distance, obj_type, stone_data = obj_data
            draw_stone(stone_data)

def hud():
    camera_text = f"Camera: Yaw {camera_yaw:.0f}° | Pitch {camera_pitch:.0f}° | Mode: {'FPV' if camera['fpv'] else 'TPV'}"
    screen_text(16, WINDOW_H - 40, camera_text)
    
    pos_text = f"Position: ({camera['x']:.1f}, {camera['y']:.1f}, {camera['z']:.1f})"
    screen_text(16, WINDOW_H - 60, pos_text)
    
    # Weather display with appropriate colors
    elapsed_time = now() - weather_start_time
    remaining_time = weather_cycle_duration - elapsed_time
    weather_display = current_weather.replace("_", " ").title()
    weather_text = f"Weather: {weather_display} ({remaining_time:.0f}s)"
    
    # Color code weather display
    weather_colors = {
        "day": (1.0, 1.0, 0.0),           # Yellow
        "evening": (1.0, 0.6, 0.0),       # Orange  
        "night": (0.4, 0.4, 1.0),         # Blue
        "early_morning": (0.7, 0.9, 1.0), # Light blue
        "cloudy": (0.7, 0.7, 0.7),        # Gray
        "rain": (0.4, 0.6, 1.0),          # Blue
        "storm": (0.6, 0.3, 0.9)          # Purple
    }
    
    weather_color = weather_colors.get(current_weather, (1.0, 1.0, 1.0))
    glColor3f(*weather_color)
    screen_text(16, WINDOW_H - 80, weather_text)
    glColor3f(1.0, 1.0, 1.0)  # Reset to white
    
    # Health display with color coding and flash effect
    health_text = f"Health: {player_health:.0f}/{max_health:.0f}"
    
    # Check if health should flash
    current_time = time.time()
    should_flash = current_time < health_flash_time and int(current_time * 10) % 2 == 0
    
    if should_flash:
        glColor3f(1.0, 0.2, 0.2)  # Bright red flash
    elif player_health > 70:
        glColor3f(0.0, 1.0, 0.0)  # Green for good health
    elif player_health > 30:
        glColor3f(1.0, 1.0, 0.0)  # Yellow for medium health
    else:
        glColor3f(1.0, 0.0, 0.0)  # Red for low health
    screen_text(16, WINDOW_H - 100, health_text)
    
    # Ammo display for both weapons (from teammate's system)
    glColor3f(1.0, 1.0, 0.8)
    rifle_ammo_text = f"Rifle Ammo: {player['rifle_ammo']}"
    screen_text(16, WINDOW_H - 120, rifle_ammo_text)
    
    pistol_ammo_text = f"Pistol Ammo: {player['pistol_ammo']}"
    screen_text(16, WINDOW_H - 140, pistol_ammo_text)
    
    # Current weapon indicator
    weapon_name = "Rifle (Blue)" if current_weapon == "left" else "Pistol (Red)" 
    weapon_color = (0.2, 0.5, 1.0) if current_weapon == "left" else (1.0, 0.2, 0.2)
    glColor3f(*weapon_color)
    weapon_text = f"Current Weapon: {weapon_name}"
    screen_text(16, WINDOW_H - 160, weapon_text)
    
    # Cheat mode indicator
    if cheat_mode:
        glColor3f(1.0, 0.0, 1.0)  # Magenta for cheat mode
        cheat_text = "CHEAT MODE: Both weapons fire!"
        screen_text(16, WINDOW_H - 180, cheat_text)
    
    glColor3f(1.0, 1.0, 1.0)  # Reset to white
    
    # Score display
    glColor3f(0.0, 1.0, 1.0)  # Cyan for score
    score_text = f"Score: {current_score:.1f}s"
    screen_text(16, WINDOW_H - 200, score_text)
    
    # Super power cheat mode status
    if cheat_mode_active:
        glColor3f(1.0, 0.8, 0.0)  # Gold for active super power
        remaining_time = cheat_mode_duration - (time.time() - cheat_activation_time)
        if remaining_time > 0:
            super_power_text = f"SUPER POWER ACTIVE! {remaining_time:.1f}s remaining"
            screen_text(16, WINDOW_H - 220, super_power_text)
    elif cheat_mode_used:
        glColor3f(0.6, 0.6, 0.6)  # Gray for used super power
        screen_text(16, WINDOW_H - 220, "Super power used (once per game)")
    else:
        glColor3f(0.8, 1.0, 0.8)  # Light green for available super power
        screen_text(16, WINDOW_H - 220, "Super power available (Press G)")
    
    # Controls
    glColor3f(0.8, 0.8, 0.8)
    controls_text = "Q: Switch Weapon | Left/Right Click: Fire | R: Restart Game | G: Super Power | I: Info | WASD: Move | Arrows: Look | Space/X: Up/Down"
    screen_text(16, 40, controls_text)
    
    if camera["night_vision"]:
        glColor3f(0.0, 1.0, 0.0)
        screen_text(16, WINDOW_H - 140, "NIGHT VISION")
    
    # Game over screen when health is zero
    if player_health <= 0:
        glColor3f(1.0, 0.0, 0.0)  # Red color for game over
        screen_text(WINDOW_W/2 - 100, WINDOW_H/2 + 60, "GAME OVER!")
        screen_text(WINDOW_W/2 - 120, WINDOW_H/2 + 30, "Health depleted!")
        screen_text(WINDOW_W/2 - 80, WINDOW_H/2, f"Final Score: {current_score:.1f} seconds")
        screen_text(WINDOW_W/2 - 140, WINDOW_H/2 - 30, "Press R to restart game & reset super power!")
        glColor3f(1.0, 1.0, 1.0)  # Reset to white
    if game_paused:
        glColor3f(1.0, 1.0, 0.0)
        screen_text(WINDOW_W/2 - 100, WINDOW_H/2 + 20, "VIEWER PAUSED")
        screen_text(WINDOW_W/2 - 120, WINDOW_H/2 - 10, "Press P to Resume")
        glColor3f(1.0, 1.0, 1.0)

last_time = now()

def idle():
    global last_time, is_walking
    cur = now()
    dt = max(0.0001, cur - last_time)
    last_time = cur

    if not game_paused:
        ensure_chunks()
        collect_active_lists()
        update_player_physics()  # Continuously update player physics from our system
        update_bullets(dt)  # Update bullets from teammate's system
        update_animals(dt)  # Update animals from teammate's system
        
        # Reset walking animation if player is not actively moving
        # This will be set to True in move_player when movement occurs
        is_walking = False

    glutPostRedisplay()

def display():
    global current_score, game_over
    
    # Update scoring system (survival time in seconds)
    if not game_over and player_health > 0:
        current_score = time.time() - game_start_time
    
    # Check for game over
    if player_health <= 0 and not game_over:
        game_over = True
        print(f"GAME OVER! Final Score: {current_score:.1f} seconds")
        print("Press 'R' to restart the game")
    
    # Update weather system
    update_weather()
    
    # Update attack effects
    update_attack_effects()
    
    # Get weather-appropriate background color
    bg = get_weather_background_color()
    
    # Apply night vision effect if enabled
    if camera["night_vision"]:
        bg = (bg[0] * 1.5, bg[1] * 1.5, bg[2] * 1.5)
    
    glClearColor(*bg, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, WINDOW_W, WINDOW_H)

    # Show the player in the game world
    setupCamera()
    draw_world()
    
    # Draw weather effects (rain, storm)
    draw_rain_effects()
    
    # Draw attack effects
    draw_attack_effects()
    
    hud()
    glutSwapBuffers()

def init_viewer():
    ensure_chunks()
    collect_active_lists()

def restart_viewer():
    global camera, chunks, last_generated_chunk
    global game_paused, last_time, camera_yaw, camera_pitch, player
    global player_pos, player_jumping, jump_velocity, in_water
    global player_health, last_damage_time
    
    camera_yaw = 0.0
    camera_pitch = 0.0
    camera.update({
        "x": 0.0, "y": 0.0, "z": CAMERA_HEIGHT,
        "fpv": True,
        "night_vision": False
    })
    
    # Reset player position and state
    player_pos.update({"x": 0.0, "y": 50.0, "z": 0.0})
    player_jumping = False
    jump_velocity = 0.0
    in_water = False

    # Reset our health system
    player_health = max_health
    last_damage_time = 0
    
    # Reset player stats (teammate's system)
    player.update({
        "health": 100,
        "max_health": 100,
        "ammo": 30,
        "last_shot_time": 0,
        "invulnerable_until": 0
    })

    foods.clear()
    ammos.clear()
    traps.clear()
    stones.clear()
    waters.clear()
    animals.clear()
    bullets.clear()
    chunks.clear()
    
    last_generated_chunk = -1
    
    game_paused = False
    last_time = now()
    
    init_viewer()
    print("Environment reset. Enjoy exploring!")

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_W, WINDOW_H)
    glutInitWindowPosition(80, 30)
    glutCreateWindow(b"Forest Environment Viewer - OpenGL")
    
    init_viewer()
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)  # Register mouse listener for weapon firing
    glutMainLoop()

if __name__ == "__main__":
    main()
