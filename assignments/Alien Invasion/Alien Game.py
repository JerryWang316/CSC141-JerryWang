import pygame
import sys
import random
import math
from pygame.sprite import Sprite, Group

# 初始化pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
DARK_BLUE = (10, 10, 40)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
LASER_BLUE = (0, 191, 255)  # 穿透激光颜色

# 游戏设置
FPS = 60
SHIP_SPEED = 5
BULLET_SPEED = 7
ALIEN_SPEED = 1.5

class Star:
    """星星背景元素"""
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.size = random.randint(1, 3)
        self.brightness = random.randint(150, 255)
        self.speed = random.uniform(0.1, 0.5)
        
    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.x = random.randint(0, SCREEN_WIDTH)
            
    def draw(self):
        color = (self.brightness, self.brightness, self.brightness)
        pygame.draw.circle(self.screen, color, (int(self.x), int(self.y)), self.size)

class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 创建缩小版飞船
        ship_width, ship_height = 35, 28
        self.image = pygame.Surface((ship_width, ship_height), pygame.SRCALPHA)
        
        pygame.draw.polygon(self.image, GREEN, [
            (17, 0), (0, 28), (14, 21), (21, 21), (35, 28)
        ])
        pygame.draw.circle(self.image, YELLOW, (17, 10), 6)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # 加速能力
        self.speed_boost = False
        self.normal_speed = SHIP_SPEED
        self.boost_speed = SHIP_SPEED * 2
        
        # 喷气特效
        self.thrust_particles = []
        self.thrust_timer = 0
        
        # 新增：穿透激光升级状态
        self.penetrating_laser = False  # 初始为普通子弹
    
    def update(self):
        """更新飞船位置和喷气特效"""
        current_speed = self.boost_speed if self.speed_boost else self.normal_speed
        dx, dy = 0, 0
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            dx += current_speed
        if self.moving_left and self.rect.left > 0:
            dx -= current_speed
        if self.moving_up and self.rect.top > 0:
            dy -= current_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            dy += current_speed
        
        # 对角线速度归一化
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071
        
        self.rect.x += dx
        self.rect.y += dy
        
        # 更新喷气特效
        self._update_thrust()
        if dx != 0 or dy != 0 or self.speed_boost:
            self._add_thrust_particles()
    
    def _add_thrust_particles(self):
        """添加喷气粒子"""
        current_time = pygame.time.get_ticks()
        if current_time - self.thrust_timer > 50:
            self.thrust_timer = current_time
            
            particle_count = 3 if self.speed_boost else 2
            for _ in range(particle_count):
                particle = {
                    'x': self.rect.centerx + random.randint(-5, 5),
                    'y': self.rect.bottom,
                    'dx': random.uniform(-0.5, 0.5),
                    'dy': random.uniform(1.0, 3.0),
                    'size': random.randint(2, 4),
                    'color': random.choice([(255, 100, 0), (255, 150, 0), (255, 200, 0)]),
                    'life': random.randint(20, 40)
                }
                self.thrust_particles.append(particle)
    
    def _update_thrust(self):
        """更新喷气粒子"""
        for particle in self.thrust_particles[:]:
            particle['x'] += particle['dx']
            particle['y'] += particle['dy']
            particle['life'] -= 1
            particle['size'] = max(0, particle['size'] - 0.1)
            
            if particle['life'] <= 0:
                self.thrust_particles.remove(particle)
    
    def _draw_thrust(self):
        """绘制喷气特效"""
        for particle in self.thrust_particles:
            alpha = int(255 * (particle['life'] / 40))
            color_with_alpha = (*particle['color'], alpha)
            
            particle_surface = pygame.Surface((int(particle['size']*2), int(particle['size']*2)), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, color_with_alpha, 
                             (int(particle['size']), int(particle['size'])), int(particle['size']))
            self.screen.blit(particle_surface, 
                           (int(particle['x'] - particle['size']), int(particle['y'] - particle['size'])))
    
    def blitme(self):
        """绘制飞船和喷气特效"""
        self._draw_thrust()
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

class Bullet(Sprite):
    def __init__(self, screen, ship, direction=0, penetrating=False):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # ============ 核心修改：根据是否穿透创建不同子弹 ============
        if not penetrating:
            # 普通子弹（缩小版）
            bullet_width, bullet_height = 4, 11
            self.image = pygame.Surface((bullet_width, bullet_height), pygame.SRCALPHA)
            for i in range(bullet_height):
                color_value = int(255 * (i / bullet_height))
                color = (255, color_value, 0)
                pygame.draw.rect(self.image, color, (0, i, bullet_width, 1))
        else:
            # 穿透激光炮（更宽、半透明、带光效）
            bullet_width, bullet_height = 20, 25  # 更宽更短
            self.image = pygame.Surface((bullet_width, bullet_height), pygame.SRCALPHA)
            # 中心亮蓝色光柱
            pygame.draw.rect(self.image, LASER_BLUE, (bullet_width//2-2, 0, 4, bullet_height))
            # 半透明外围光晕
            for offset in [0, 3, 6]:
                alpha = 100 - offset*10
                glow_color = (0, 191, 255, alpha)
                glow_surf = pygame.Surface((bullet_width-offset*2, bullet_height), pygame.SRCALPHA)
                pygame.draw.rect(glow_surf, glow_color, (0, 0, bullet_width-offset*2, bullet_height))
                self.image.blit(glow_surf, (offset, 0))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.centery
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # ============ 核心修改：射击方向默认为0（竖直向上） ============
        self.direction = direction  # 0 = 向上，玩家仍可按1-6键改变方向
        self.speed = BULLET_SPEED
        
        # 子弹属性
        self.penetrating = penetrating  # 是否具有穿透能力
        self.trail = []
        self.trail_length = 5
    
    def update(self):
        """移动子弹"""
        self.trail.append((self.rect.centerx, self.rect.centery))
        if len(self.trail) > self.trail_length:
            self.trail.pop(0)
        
        self.x += math.cos(self.direction) * self.speed
        self.y -= math.sin(self.direction) * self.speed
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        # 如果子弹移出屏幕则移除
        if (self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or 
            self.rect.right < 0 or self.rect.left > SCREEN_WIDTH):
            self.kill()
    
    def draw_bullet(self):
        """绘制子弹及其尾迹"""
        for i, pos in enumerate(self.trail):
            if self.penetrating:
                # 穿透激光的尾迹更亮
                alpha = int(150 * (i / len(self.trail)))
                trail_color = (100, 200, 255, alpha)
                size = max(2, i//1.5)
            else:
                alpha = int(255 * (i / len(self.trail)))
                trail_color = (255, int(alpha/2), 0, alpha)
                size = max(1, i//2)
            pygame.draw.circle(self.screen, trail_color, pos, int(size))
        
        self.screen.blit(self.image, self.rect)

class Alien(Sprite):
    def __init__(self, screen, alien_type=1):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.alien_type = alien_type
        
        if alien_type == 1:
            self._create_type1()
        else:
            self._create_type2()
        
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.horizontal_speed = random.uniform(-0.5, 0.5)
        
        self.pulse_size = 1.0
        self.pulse_speed = random.uniform(0.01, 0.03)
        
        # 类型2的特殊属性
        if alien_type == 2:
            self.health = 2
            self.horizontal_speed = random.uniform(-1.0, 1.0)
        else:
            self.health = 1
    
    def _create_type1(self):
        """类型1外星人（标准）"""
        alien_width, alien_height = 28, 28
        self.image = pygame.Surface((alien_width, alien_height), pygame.SRCALPHA)
        
        for r in range(10, 0, -1):
            color_value = int(255 * (r / 10))
            pygame.draw.circle(self.image, (0, 0, color_value), (14, 14), r)
        
        pygame.draw.circle(self.image, (200, 200, 255), (8, 10), 5)
        pygame.draw.circle(self.image, (200, 200, 255), (20, 10), 5)
        pygame.draw.circle(self.image, WHITE, (8, 10), 3)
        pygame.draw.circle(self.image, WHITE, (20, 10), 3)
        pygame.draw.circle(self.image, BLACK, (8, 10), 2)
        pygame.draw.circle(self.image, BLACK, (20, 10), 2)
        
        pygame.draw.arc(self.image, RED, (7, 14, 14, 7), 0, math.pi, 2)
        
        self.rect = self.image.get_rect()
    
    def _create_type2(self):
        """类型2外星人（高级）"""
        alien_width, alien_height = 32, 32
        self.image = pygame.Surface((alien_width, alien_height), pygame.SRCALPHA)
        
        pygame.draw.polygon(self.image, PURPLE, [(16, 0), (0, 32), (32, 32)])
        pygame.draw.polygon(self.image, (180, 0, 180), [(16, 5), (8, 25), (24, 25)])
        
        pygame.draw.circle(self.image, CYAN, (10, 12), 4)
        pygame.draw.circle(self.image, CYAN, (22, 12), 4)
        pygame.draw.circle(self.image, WHITE, (10, 12), 2)
        pygame.draw.circle(self.image, WHITE, (22, 12), 2)
        
        for i in range(5):
            x_pos = 6 + i * 5
            pygame.draw.line(self.image, ORANGE, (x_pos, 30), (x_pos, 24), 2)
        
        self.rect = self.image.get_rect()
    
    def update(self):
        self.y += ALIEN_SPEED
        self.x += self.horizontal_speed
        
        self.pulse_size = 1.0 + 0.1 * math.sin(pygame.time.get_ticks() * self.pulse_speed)
        
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            self.horizontal_speed *= -1
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
    
    def hit(self):
        """外星人被击中"""
        self.health -= 1
        return self.health <= 0
    
    def blitme(self):
        """绘制外星人及其脉动效果"""
        if self.alien_type == 1:
            current_size = int(28 * self.pulse_size)
        else:
            current_size = int(32 * self.pulse_size)
            
        scaled_image = pygame.transform.scale(self.image, (current_size, current_size))
        scaled_rect = scaled_image.get_rect(center=self.rect.center)
        self.screen.blit(scaled_image, scaled_rect)
        
        # 为类型2外星人绘制生命条
        if self.alien_type == 2 and self.health < 2:
            health_width = 30
            health_height = 4
            health_x = self.rect.centerx - health_width // 2
            health_y = self.rect.top - 10
            
            pygame.draw.rect(self.screen, (100, 100, 100), (health_x, health_y, health_width, health_height))
            health_percent = self.health / 2
            pygame.draw.rect(self.screen, GREEN, (health_x, health_y, int(health_width * health_percent), health_height))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("增强版太空入侵者 - 穿透激光升级")
        self.clock = pygame.time.Clock()
        
        # 创建星空背景
        self.stars = [Star(self.screen) for _ in range(100)]
        
        # 创建游戏对象
        self.ship = Ship(self.screen)
        self.bullets = Group()
        self.aliens = Group()
        
        # 游戏状态
        self.score = 0
        self.level = 1
        self.game_active = True
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 48)
        
        # 外星人生成计时器
        self.alien_spawn_time = 0
        self.alien_spawn_delay = 1500
        
        # ============ 核心修改：射击方向默认为0（竖直向上） ============
        self.bullet_direction = 0  # 0弧度 = 竖直向上
        
        # 添加爆炸粒子效果列表
        self.explosions = []
        
        # 添加背景行星
        self.planets = []
        self._create_background_planets()
    
    def _create_background_planets(self):
        """创建背景行星"""
        for _ in range(3):
            planet = {
                'x': random.randint(0, SCREEN_WIDTH),
                'y': random.randint(0, SCREEN_HEIGHT),
                'radius': random.randint(20, 60),
                'color': (random.randint(50, 100), random.randint(50, 100), random.randint(100, 150)),
                'speed': random.uniform(0.05, 0.15)
            }
            self.planets.append(planet)
    
    def _update_background(self):
        """更新背景元素"""
        for star in self.stars:
            star.update()
        
        for planet in self.planets:
            planet['y'] += planet['speed']
            if planet['y'] > SCREEN_HEIGHT + planet['radius']:
                planet['y'] = -planet['radius']
                planet['x'] = random.randint(0, SCREEN_WIDTH)
    
    def _draw_background(self):
        """绘制背景"""
        self.screen.fill(DARK_BLUE)
        
        for planet in self.planets:
            pygame.draw.circle(self.screen, planet['color'], 
                             (int(planet['x']), int(planet['y'])), planet['radius'])
            pygame.draw.circle(self.screen, (planet['color'][0]+20, planet['color'][1]+20, planet['color'][2]+20), 
                             (int(planet['x']), int(planet['y'])), planet['radius'] + 5, 2)
        
        for star in self.stars:
            star.draw()
        
        for _ in range(20):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            size = random.randint(1, 2)
            brightness = random.randint(50, 100)
            pygame.draw.circle(self.screen, (brightness, brightness, brightness), (x, y), size)
    
    def _create_explosion(self, x, y, size_multiplier=1.0):
        """创建爆炸粒子效果"""
        particle_count = int(15 * size_multiplier)
        for _ in range(particle_count):
            particle = {
                'x': x,
                'y': y,
                'dx': random.uniform(-3, 3),
                'dy': random.uniform(-3, 3),
                'size': random.randint(2, 5) * size_multiplier,
                'color': (random.randint(200, 255), random.randint(100, 200), 0),
                'life': random.randint(20, 40)
            }
            self.explosions.append(particle)
    
    def _update_explosions(self):
        """更新爆炸粒子"""
        for explosion in self.explosions[:]:
            explosion['x'] += explosion['dx']
            explosion['y'] += explosion['dy']
            explosion['life'] -= 1
            explosion['size'] = max(0, explosion['size'] - 0.1)
            
            if explosion['life'] <= 0:
                self.explosions.remove(explosion)
    
    def _draw_explosions(self):
        """绘制爆炸粒子"""
        for explosion in self.explosions:
            alpha = int(255 * (explosion['life'] / 40))
            color_with_alpha = (*explosion['color'], alpha)
            
            particle_surface = pygame.Surface((int(explosion['size']*2), int(explosion['size']*2)), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, color_with_alpha, 
                             (int(explosion['size']), int(explosion['size'])), int(explosion['size']))
            self.screen.blit(particle_surface, 
                           (int(explosion['x'] - explosion['size']), int(explosion['y'] - explosion['size'])))
    
    def run_game(self):
        """主游戏循环"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._spawn_aliens()
                self._check_collisions()
                self._update_explosions()
                self._update_level()  # 检查等级更新
            
            self._update_background()
            self._update_screen()
            self.clock.tick(FPS)
    
    def _check_events(self):
        """响应按键事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_LSHIFT:
                    self.ship.speed_boost = True
                elif event.key == pygame.K_1:
                    self.bullet_direction = 0  # 上
                elif event.key == pygame.K_2:
                    self.bullet_direction = math.pi/2  # 右
                elif event.key == pygame.K_3:
                    self.bullet_direction = math.pi  # 下
                elif event.key == pygame.K_4:
                    self.bullet_direction = 3*math.pi/2  # 左
                elif event.key == pygame.K_5:
                    self.bullet_direction = math.pi/4  # 右上
                elif event.key == pygame.K_6:
                    self.bullet_direction = 3*math.pi/4  # 左上
                elif event.key == pygame.K_r and not self.game_active:
                    self._restart_game()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                elif event.key == pygame.K_LSHIFT:
                    self.ship.speed_boost = False
    
    def _fire_bullet(self):
        """创建新子弹"""
        if len(self.bullets) < 15:  # 增加子弹上限
            # ============ 核心修改：根据飞船状态创建不同类型的子弹 ============
            penetrating = self.ship.penetrating_laser
            new_bullet = Bullet(self.screen, self.ship, self.bullet_direction, penetrating)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """更新子弹位置"""
        self.bullets.update()
    
    def _update_aliens(self):
        """更新外星人位置"""
        self.aliens.update()
    
    def _spawn_aliens(self):
        """定期生成新外星人"""
        current_time = pygame.time.get_ticks()
        if current_time - self.alien_spawn_time > self.alien_spawn_delay:
            # 根据等级决定生成哪种外星人
            alien_type = 1 if random.random() < 0.7 or self.level < 2 else random.choice([1, 2])
            new_alien = Alien(self.screen, alien_type)
            self.aliens.add(new_alien)
            self.alien_spawn_time = current_time
    
    def _check_collisions(self):
        """检查碰撞"""
        # 检查子弹-外星人碰撞
        for bullet in self.bullets.sprites():
            aliens_hit = pygame.sprite.spritecollide(bullet, self.aliens, False)
            if aliens_hit:
                # ============ 核心修改：穿透激光逻辑 ============
                if bullet.penetrating:
                    # 穿透激光：击中所有碰撞的外星人，子弹不消失
                    for alien in aliens_hit:
                        if alien.hit():
                            self.score += 10 if alien.alien_type == 1 else 20
                            self.aliens.remove(alien)
                            size_multiplier = 1.5 if alien.alien_type == 2 else 1.0
                            self._create_explosion(alien.rect.centerx, alien.rect.centery, size_multiplier)
                else:
                    # 普通子弹：只击中第一个外星人，然后子弹消失
                    if aliens_hit:
                        alien = aliens_hit[0]
                        if alien.hit():
                            self.score += 10 if alien.alien_type == 1 else 20
                            self.aliens.remove(alien)
                            size_multiplier = 1.5 if alien.alien_type == 2 else 1.0
                            self._create_explosion(alien.rect.centerx, alien.rect.centery, size_multiplier)
                        bullet.kill()  # 普通子弹击中后消失
        
        # 检查外星人-飞船碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.game_active = False
            self._create_explosion(self.ship.rect.centerx, self.ship.rect.centery, 2.0)
        
        # 检查外星人是否到达底部
        for alien in self.aliens:
            if alien.rect.bottom >= SCREEN_HEIGHT:
                self.game_active = False
                break
    
    def _update_level(self):
        """更新游戏等级和飞船升级"""
        # 每100分升一级
        new_level = self.score // 100 + 1
        if new_level > self.level:
            self.level = new_level
            # 随着等级提高，外星人生成更快
            self.alien_spawn_delay = max(500, 1500 - (self.level * 100))
            
            # ============ 核心修改：等级≥2时解锁穿透激光 ============
            if self.level >= 2 and not self.ship.penetrating_laser:
                self.ship.penetrating_laser = True
                # 飞船视觉升级提示（可在此处添加升级特效）
                self.ship.image.fill((0, 0, 0, 0))  # 清空原有图像
                # 绘制升级版飞船（带激光炮特效）
                pygame.draw.polygon(self.ship.image, (0, 255, 100), [  # 更亮的绿色
                    (17, 0), (0, 28), (14, 21), (21, 21), (35, 28)
                ])
                pygame.draw.circle(self.ship.image, (255, 255, 150), (17, 10), 6)  # 更亮的驾驶舱
                # 在飞船两侧添加激光炮管
                pygame.draw.rect(self.ship.image, (200, 200, 200), (5, 15, 4, 8))
                pygame.draw.rect(self.ship.image, (200, 200, 200), (26, 15, 4, 8))
    
    def _update_screen(self):
        """更新屏幕"""
        self._draw_background()
        self._draw_explosions()
        
        # 绘制游戏对象
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.blitme()
        
        # 绘制游戏标题
        title_text = self.title_font.render("太空保卫者 - 激光升级版", True, (100, 200, 255))
        self.screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 5))
        
        # 绘制信息面板
        info_panel = pygame.Surface((300, 180), pygame.SRCALPHA)
        info_panel.fill((0, 0, 0, 150))
        self.screen.blit(info_panel, (10, 10))
        
        # 分数和等级
        score_text = self.font.render(f"分数: {self.score}", True, YELLOW)
        self.screen.blit(score_text, (20, 20))
        
        level_text = self.font.render(f"等级: {self.level}", True, YELLOW)
        self.screen.blit(level_text, (20, 60))
        
        # 下一等级提示
        next_level_text = self.small_font.render(f"下一等级: {100 - (self.score % 100)} 分", True, CYAN)
        self.screen.blit(next_level_text, (20, 100))
        
        # 武器状态
        weapon_color = LASER_BLUE if self.ship.penetrating_laser else (200, 200, 200)
        weapon_text = self.small_font.render(
            f"武器: {'🔷 穿透激光' if self.ship.penetrating_laser else '🔶 普通子弹'}", 
            True, weapon_color
        )
        self.screen.blit(weapon_text, (20, 140))
        
        # 控制面板
        controls_panel = pygame.Surface((500, 100), pygame.SRCALPHA)
        controls_panel.fill((0, 0, 0, 150))
        self.screen.blit(controls_panel, (SCREEN_WIDTH - 510, 10))
        
        controls_text = self.small_font.render("控制: 方向键=移动, 空格=射击, Shift=加速, 1-6=方向", True, GREEN)
        self.screen.blit(controls_text, (SCREEN_WIDTH - 500, 20))
        
        # 子弹方向指示器
        direction_names = {
            0: "↑ 上", math.pi/4: "↗ 右上", math.pi/2: "→ 右",
            3*math.pi/4: "↘ 右下", math.pi: "↓ 下",
            5*math.pi/4: "↙ 左下", 3*math.pi/2: "← 左",
            7*math.pi/4: "↖ 左上"
        }
        direction_text = self.small_font.render(
            f"子弹方向: {direction_names.get(self.bullet_direction, '自定义')}", 
            True, PURPLE
        )
        self.screen.blit(direction_text, (SCREEN_WIDTH - 500, 50))
        
        # 速度指示器
        speed_color = (0, 255, 0) if self.ship.speed_boost else (200, 200, 200)
        speed_text = self.small_font.render(
            f"速度: {'⚡ 加速' if self.ship.speed_boost else '● 正常'}", 
            True, speed_color
        )
        self.screen.blit(speed_text, (SCREEN_WIDTH - 500, 80))
        
        # 游戏结束屏幕
        if not self.game_active:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.screen.blit(overlay, (0, 0))
            
            game_over_text = self.title_font.render("任务失败", True, RED)
            score_display = self.font.render(f"最终分数: {self.score}", True, YELLOW)
            restart_text = self.font.render("按 [R] 键重新开始任务", True, WHITE)
            
            self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2 - 60))
            self.screen.blit(score_display, (SCREEN_WIDTH//2 - score_display.get_width()//2, SCREEN_HEIGHT//2))
            self.screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 50))
        
        pygame.display.flip()
    
    def _restart_game(self):
        """重新开始游戏"""
        self.game_active = True
        self.score = 0
        self.level = 1
        self.bullets.empty()
        self.aliens.empty()
        self.explosions.clear()
        self.ship.center_ship()
        # ============ 核心修改：重置射击方向和飞船状态 ============
        self.bullet_direction = 0  # 重置为默认向上射击
        self.ship.penetrating_laser = False  # 重置为普通子弹
        self.alien_spawn_delay = 1500
        # 重置飞船外观
        self.ship.image.fill((0, 0, 0, 0))
        pygame.draw.polygon(self.ship.image, GREEN, [
            (17, 0), (0, 28), (14, 21), (21, 21), (35, 28)
        ])
        pygame.draw.circle(self.ship.image, YELLOW, (17, 10), 6)

if __name__ == '__main__':
    ai_game = Game()
    ai_game.run_game()