# #=============================================================================================================================
# # Code for the Multi-commodity Flows problem (Arc version) for lectures of course AE4423 (Airline Planning & Optimisation)
# #=============================================================================================================================
from gurobipy import *
from openpyxl import *
from time import *


# =============================================================================================================================
#  Create the model which represent the nodes, arcs, and comodities
# =============================================================================================================================
from dataclasses import dataclass

@dataclass(frozen=True)
class HangarConfig:              # scalars, Section 3.3
    HW: float = 65.0             # [m]
    HL: float = 60.0             # [m]
    buffer: float = 5.0          # [m]
    eps_t: float = 0.1           # [h]
    eps_p: float = 1e-3          # objective only; placeholder value

@dataclass
class Aircraft:                  # parameters, Section 3.4
    name: str
    W: float
    L: float
    ETA: float
    ETD: float
    serv_time: float
    P_rej: float = 0.0
    P_arr: float = 0.0
    P_dep: float = 0.0
    x_init: float | None = None  # only set for aircraft already inside (set C)
    y_init: float | None = None

class HangarModel:
    def __init__(self, cfg: HangarConfig, aircraft: list[Aircraft]):
        self.cfg = cfg
        self.C = [a for a in aircraft if a.x_init is not None]
        self.F = [a for a in aircraft if a.x_init is None]
        self.A = self.C + self.F
        self.M_X, self.M_Y = cfg.HW, cfg.HL
        self.M_T = (max((f.ETA for f in self.F), default=0.0)
                    + sum(a.serv_time for a in self.A)
                    + 2 * len(self.A) * cfg.eps_t)
        # then create variables and add constraint groups:
        # (2)-(6) acceptance, (7)-(10) walls, (11)-(13) separation,
        # (14)-(20) sequencing, (21)-(22) blocking, (23)-(29) initial state



# =============================================================================================================================
#  Run the Program
# =============================================================================================================================
if __name__ == '__main__':
    Arcs, Nodes, Commodities = construct_graph()

    # RUN MCF PROBLEM
    start_time = time()
    MCF_Problem(Arcs, Nodes, Commodities)
    print('Run Time =', time() - start_time)






