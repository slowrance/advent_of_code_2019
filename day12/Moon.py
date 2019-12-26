from __future__ import annotations

class Moon():
    def __init__(self, x_pos, y_pos, z_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0
        self.x_change = 0
        self.y_change = 0
        self.z_change = 0

    def __repr__(self):
        return f'pos=<x={self.x_pos}, y={self.y_pos}, z={self.z_pos}>, vel=<x={self.x_vel}, y={self.y_vel}, z={self.z_vel}>'

    def calc_gravity(self, other: Moon):
        if self.x_pos < other.x_pos:
            self.x_change += 1
        elif self.x_pos > other.x_pos:
            self.x_change -= 1
        if self.y_pos < other.y_pos:
            self.y_change += 1
        elif self.y_pos > other.y_pos:
            self.y_change -= 1
        if self.z_pos < other.z_pos:
            self.z_change += 1
        elif self.z_pos > other.z_pos:
            self.z_change -= 1

    def change_vel(self):
        self.x_vel += self.x_change
        self.y_vel += self.y_change
        self.z_vel += self.z_change
        self.x_change = 0
        self.y_change = 0
        self.z_change = 0

    def change_pos(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.z_pos += self.z_vel

    def calc_energy(self):
        self.pot_energy = abs(self.x_pos) + abs(self.y_pos) + abs(self.z_pos)
        self.kin_energy = abs(self.x_vel) + abs(self.y_vel) + abs(self.z_vel)
        self.total_energy = self.pot_energy * self.kin_energy
        return f'PE = {self.pot_energy}; KE = {self.kin_energy}; Total Energy = {self.total_energy}'

    def curr_state(self):
        return (self.x_pos, self.y_pos, self.z_pos), (self.x_vel, self.y_vel, self.z_vel)

