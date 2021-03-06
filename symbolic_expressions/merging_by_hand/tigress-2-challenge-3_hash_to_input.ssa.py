#!/usr/bin/env python2
## -*- coding: utf-8 -*-
##
## Triton
##

import sys
import z3

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

ctx = z3.Context()
s   = z3.Solver()

SymVar_0 = z3.BitVec('SymVar_0', 64)

guard_334 = SymVar_0
guard_349 = guard_334 # MOV operation
guard_14284 = guard_349 # MOV operation
guard_14836 = guard_14284 # MOV operation
guard_14844 = ((0x2A766E54 + guard_14836) & 0xFFFFFFFFFFFFFFFF) # ADD operation
guard_15154 = guard_14844 # MOV operation
guard_15170 = guard_15154 # MOV operation
guard_15174 = ((guard_15170 << (0x5 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
guard_15181 = guard_15174 # MOV operation
guard_17493 = guard_349 # MOV operation
guard_18097 = guard_17493 # MOV operation
guard_18105 = ((0x2A766E54 + guard_18097) & 0xFFFFFFFFFFFFFFFF) # ADD operation
guard_18681 = guard_18105 # MOV operation
guard_18689 = guard_18681 # MOV operation
guard_18693 = (guard_18689 >> (0x3B & 0x3F)) # SHR operation
guard_18700 = guard_18693 # MOV operation
guard_19012 = guard_15181 # MOV operation
guard_19018 = guard_18700 # MOV operation
guard_19020 = (guard_19018 | guard_19012) # OR operation
guard_19285 = guard_19020 # MOV operation
guard_23773 = guard_349 # MOV operation
guard_26470 = guard_19285 # MOV operation
guard_26756 = guard_26470 # MOV operation
guard_26784 = (((0x0) << 64 | guard_26756) / (((((((((0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x5 & 0xFF))) # DIV operation
guard_27045 = guard_23773 # MOV operation
guard_27051 = guard_26784 # MOV operation
guard_27053 = ((guard_27051 + guard_27045) & 0xFFFFFFFFFFFFFFFF) # ADD operation
guard_27355 = guard_27053 # MOV operation
guard_31854 = guard_349 # MOV operation
guard_32432 = guard_31854 # MOV operation
guard_32440 = guard_32432 # MOV operation
guard_32442 = ((guard_32440 - 0x18E8E014) & 0xFFFFFFFFFFFFFFFF) # SUB operation
guard_32450 = guard_32442 # MOV operation
guard_35140 = guard_19285 # MOV operation
guard_35743 = guard_35140 # MOV operation
guard_35751 = ((0xB70D976 + guard_35743) & 0xFFFFFFFFFFFFFFFF) # ADD operation
guard_36037 = guard_35751 # MOV operation
guard_36039 = ((guard_36037 + 0x2E281C99) & 0xFFFFFFFFFFFFFFFF) # ADD operation
guard_36357 = guard_32450 # MOV operation
guard_36363 = guard_36039 # MOV operation
guard_36365 = guard_36357 # MOV operation
guard_36367 = ((guard_36365 - guard_36363) & 0xFFFFFFFFFFFFFFFF) # SUB operation
guard_36375 = guard_36367 # MOV operation
guard_36635 = guard_36375 # MOV operation
guard_36637 = ((guard_36635 >> 56) & 0xFF) # Byte reference - MOV operation
guard_36638 = ((guard_36635 >> 48) & 0xFF) # Byte reference - MOV operation
guard_36639 = ((guard_36635 >> 40) & 0xFF) # Byte reference - MOV operation
guard_36640 = ((guard_36635 >> 32) & 0xFF) # Byte reference - MOV operation
guard_36641 = ((guard_36635 >> 24) & 0xFF) # Byte reference - MOV operation
guard_36642 = ((guard_36635 >> 16) & 0xFF) # Byte reference - MOV operation
guard_36643 = ((guard_36635 >> 8) & 0xFF) # Byte reference - MOV operation
guard_36644 = (guard_36635 & 0xFF) # Byte reference - MOV operation
guard_46172 = (guard_36642 & 0xFF) # MOVZX operation
guard_46724 = (guard_46172 & 0xFF) # MOVZX operation
guard_50883 = (guard_36637 & 0xFF) # MOVZX operation
guard_55035 = (guard_50883 & 0xFF) # MOVZX operation
guard_55037 = ((guard_55035 & 0xFF) & 0xFF) # Byte reference - MOV operation
guard_55627 = (guard_46724 & 0xFF) # MOVZX operation
guard_59732 = (guard_55627 & 0xFF) # MOVZX operation
guard_59734 = ((guard_59732 & 0xFF) & 0xFF) # Byte reference - MOV operation
guard_62432 = guard_19285 # MOV operation
guard_64845 = guard_27355 # MOV operation
guard_65101 = guard_62432 # MOV operation
guard_65107 = guard_64845 # MOV operation
guard_65109 = ((guard_65107 + guard_65101) & 0xFFFFFFFFFFFFFFFF) # ADD operation
guard_67830 = (((((((((guard_59734 & 0xFF)) << 8 | (guard_36638 & 0xFF)) << 8 | (guard_36639 & 0xFF)) << 8 | (guard_36640 & 0xFF)) << 8 | (guard_36641 & 0xFF)) << 8 | (guard_55037 & 0xFF)) << 8 | (guard_36643 & 0xFF)) << 8 | (guard_36644 & 0xFF)) # MOV operation
guard_68104 = guard_67830 # MOV operation
guard_68132 = (((0x0) << 64 | guard_68104) / (((((((((0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x8 & 0xFF))) # DIV operation
guard_68445 = guard_65109 # MOV operation
guard_68451 = guard_68132 # MOV operation
guard_68453 = ((guard_68445 - guard_68451) & 0xFFFFFFFFFFFFFFFF) # CMP operation
guard_68455 = ((((guard_68445 ^ (guard_68451 ^ guard_68453)) ^ ((guard_68445 ^ guard_68453) & (guard_68445 ^ guard_68451))) >> 63) & 0x1) # Carry flag
guard_68461 = ((((guard_68451 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((guard_68455 & 0x1) == 0x1) else 0x0)) # SETB operation
guard_68463 = (guard_68461 & 0xFF) # MOVZX operation
guard_68731 = (guard_68463 & 0xFFFFFFFF) # MOV operation
guard_68733 = ((guard_68731 & 0xFFFFFFFF) & (guard_68731 & 0xFFFFFFFF)) # TEST operation
guard_68738 = (0x1 if ((guard_68733 & 0xFFFFFFFF) == 0x0) else 0x0) # Zero flag

branch1_334 = SymVar_0
branch1_349 = branch1_334 # MOV operation
branch1_14284 = branch1_349 # MOV operation
branch1_14836 = branch1_14284 # MOV operation
branch1_14844 = ((0x2A766E54 + branch1_14836) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch1_15154 = branch1_14844 # MOV operation
branch1_15170 = branch1_15154 # MOV operation
branch1_15174 = ((branch1_15170 << (0x5 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch1_15181 = branch1_15174 # MOV operation
branch1_17493 = branch1_349 # MOV operation
branch1_18097 = branch1_17493 # MOV operation
branch1_18105 = ((0x2A766E54 + branch1_18097) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch1_18681 = branch1_18105 # MOV operation
branch1_18689 = branch1_18681 # MOV operation
branch1_18693 = (branch1_18689 >> (0x3B & 0x3F)) # SHR operation
branch1_18700 = branch1_18693 # MOV operation
branch1_19012 = branch1_15181 # MOV operation
branch1_19018 = branch1_18700 # MOV operation
branch1_19020 = (branch1_19018 | branch1_19012) # OR operation
branch1_19285 = branch1_19020 # MOV operation
branch1_23773 = branch1_349 # MOV operation
branch1_26470 = branch1_19285 # MOV operation
branch1_26756 = branch1_26470 # MOV operation
branch1_26784 = (((0x0) << 64 | branch1_26756) / (((((((((0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x5 & 0xFF))) # DIV operation
branch1_27045 = branch1_23773 # MOV operation
branch1_27051 = branch1_26784 # MOV operation
branch1_27053 = ((branch1_27051 + branch1_27045) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch1_27355 = branch1_27053 # MOV operation
branch1_31854 = branch1_349 # MOV operation
branch1_32432 = branch1_31854 # MOV operation
branch1_32440 = branch1_32432 # MOV operation
branch1_32442 = ((branch1_32440 - 0x18E8E014) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch1_32450 = branch1_32442 # MOV operation
branch1_35140 = branch1_19285 # MOV operation
branch1_35743 = branch1_35140 # MOV operation
branch1_35751 = ((0xB70D976 + branch1_35743) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch1_36037 = branch1_35751 # MOV operation
branch1_36039 = ((branch1_36037 + 0x2E281C99) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch1_36357 = branch1_32450 # MOV operation
branch1_36363 = branch1_36039 # MOV operation
branch1_36365 = branch1_36357 # MOV operation
branch1_36367 = ((branch1_36365 - branch1_36363) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch1_36375 = branch1_36367 # MOV operation
branch1_36635 = branch1_36375 # MOV operation
branch1_36637 = ((branch1_36635 >> 56) & 0xFF) # Byte reference - MOV operation
branch1_36638 = ((branch1_36635 >> 48) & 0xFF) # Byte reference - MOV operation
branch1_36639 = ((branch1_36635 >> 40) & 0xFF) # Byte reference - MOV operation
branch1_36640 = ((branch1_36635 >> 32) & 0xFF) # Byte reference - MOV operation
branch1_36641 = ((branch1_36635 >> 24) & 0xFF) # Byte reference - MOV operation
branch1_36642 = ((branch1_36635 >> 16) & 0xFF) # Byte reference - MOV operation
branch1_36643 = ((branch1_36635 >> 8) & 0xFF) # Byte reference - MOV operation
branch1_36644 = (branch1_36635 & 0xFF) # Byte reference - MOV operation
branch1_41119 = branch1_349 # MOV operation
branch1_41709 = branch1_41119 # MOV operation
branch1_41717 = ((0x3FB85732 + branch1_41709) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch1_41997 = branch1_41717 # MOV operation
branch1_46172 = (branch1_36642 & 0xFF) # MOVZX operation
branch1_46724 = (branch1_46172 & 0xFF) # MOVZX operation
branch1_50883 = (branch1_36637 & 0xFF) # MOVZX operation
branch1_55035 = (branch1_50883 & 0xFF) # MOVZX operation
branch1_55037 = ((branch1_55035 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch1_55627 = (branch1_46724 & 0xFF) # MOVZX operation
branch1_59732 = (branch1_55627 & 0xFF) # MOVZX operation
branch1_59734 = ((branch1_59732 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch1_73780 = (((((((((branch1_59734 & 0xFF)) << 8 | (branch1_36638 & 0xFF)) << 8 | (branch1_36639 & 0xFF)) << 8 | (branch1_36640 & 0xFF)) << 8 | (branch1_36641 & 0xFF)) << 8 | (branch1_55037 & 0xFF)) << 8 | (branch1_36643 & 0xFF)) << 8 | (branch1_36644 & 0xFF)) # MOV operation
branch1_76211 = branch1_41997 # MOV operation
branch1_76763 = branch1_76211 # MOV operation
branch1_76771 = branch1_76763 # MOV operation
branch1_76775 = (branch1_76771 >> (0x7 & 0x3F)) # SHR operation
branch1_76782 = branch1_76775 # MOV operation
branch1_79497 = branch1_41997 # MOV operation
branch1_79771 = branch1_79497 # MOV operation
branch1_79787 = branch1_79771 # MOV operation
branch1_79791 = ((branch1_79787 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch1_79798 = branch1_79791 # MOV operation
branch1_80110 = branch1_76782 # MOV operation
branch1_80116 = branch1_79798 # MOV operation
branch1_80118 = (branch1_80116 | branch1_80110) # OR operation
branch1_80409 = branch1_73780 # MOV operation
branch1_80415 = branch1_80118 # MOV operation
branch1_80417 = ((branch1_80415 + branch1_80409) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch1_81019 = branch1_80417 # MOV operation
branch1_81027 = branch1_81019 # MOV operation
branch1_81031 = (branch1_81027 >> (0x2 & 0x3F)) # SHR operation
branch1_81038 = branch1_81031 # MOV operation
branch1_81290 = branch1_81038 # MOV operation
branch1_81306 = (0xF & branch1_81290) # AND operation
branch1_81921 = branch1_81306 # MOV operation
branch1_81929 = (0x1 | branch1_81921) # OR operation
branch1_84649 = branch1_27355 # MOV operation
branch1_85213 = branch1_84649 # MOV operation
branch1_85221 = branch1_85213 # MOV operation
branch1_85225 = (branch1_85221 >> (0x1 & 0x3F)) # SHR operation
branch1_85232 = branch1_85225 # MOV operation
branch1_85520 = branch1_85232 # MOV operation
branch1_85536 = (0xF & branch1_85520) # AND operation
branch1_86162 = branch1_85536 # MOV operation
branch1_86170 = (0x1 | branch1_86162) # OR operation
branch1_88573 = branch1_19285 # MOV operation
branch1_88859 = branch1_88573 # MOV operation
branch1_88873 = branch1_86170 # MOV operation
branch1_88875 = branch1_88859 # MOV operation
branch1_88877 = (branch1_88873 & 0xFFFFFFFF) # MOV operation
branch1_88879 = ((branch1_88875 << ((branch1_88877 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch1_88886 = branch1_88879 # MOV operation
branch1_91279 = branch1_19285 # MOV operation
branch1_94290 = branch1_27355 # MOV operation
branch1_94854 = branch1_94290 # MOV operation
branch1_94862 = branch1_94854 # MOV operation
branch1_94866 = (branch1_94862 >> (0x1 & 0x3F)) # SHR operation
branch1_94873 = branch1_94866 # MOV operation
branch1_95161 = branch1_94873 # MOV operation
branch1_95177 = (0xF & branch1_95161) # AND operation
branch1_95804 = branch1_95177 # MOV operation
branch1_95812 = (0x1 | branch1_95804) # OR operation
branch1_96109 = branch1_95812 # MOV operation
branch1_96113 = ((0x40 - branch1_96109) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch1_96121 = branch1_96113 # MOV operation
branch1_96395 = branch1_91279 # MOV operation
branch1_96401 = branch1_96121 # MOV operation
branch1_96403 = branch1_96395 # MOV operation
branch1_96405 = (branch1_96401 & 0xFFFFFFFF) # MOV operation
branch1_96407 = (branch1_96403 >> ((branch1_96405 & 0xFF) & 0x3F)) # SHR operation
branch1_96414 = branch1_96407 # MOV operation
branch1_96726 = branch1_88886 # MOV operation
branch1_96732 = branch1_96414 # MOV operation
branch1_96734 = (branch1_96732 | branch1_96726) # OR operation
branch1_96991 = branch1_96734 # MOV operation
branch1_97005 = branch1_81929 # MOV operation
branch1_97007 = branch1_96991 # MOV operation
branch1_97009 = (branch1_97005 & 0xFFFFFFFF) # MOV operation
branch1_97011 = ((branch1_97007 << ((branch1_97009 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch1_97018 = branch1_97011 # MOV operation
branch1_99773 = branch1_27355 # MOV operation
branch1_100325 = branch1_99773 # MOV operation
branch1_100333 = branch1_100325 # MOV operation
branch1_100337 = (branch1_100333 >> (0x1 & 0x3F)) # SHR operation
branch1_100344 = branch1_100337 # MOV operation
branch1_100648 = branch1_100344 # MOV operation
branch1_100664 = (0xF & branch1_100648) # AND operation
branch1_101235 = branch1_100664 # MOV operation
branch1_101243 = (0x1 | branch1_101235) # OR operation
branch1_103697 = branch1_19285 # MOV operation
branch1_103957 = branch1_103697 # MOV operation
branch1_103971 = branch1_101243 # MOV operation
branch1_103973 = branch1_103957 # MOV operation
branch1_103975 = (branch1_103971 & 0xFFFFFFFF) # MOV operation
branch1_103977 = ((branch1_103973 << ((branch1_103975 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch1_103984 = branch1_103977 # MOV operation
branch1_106407 = branch1_19285 # MOV operation
branch1_109393 = branch1_27355 # MOV operation
branch1_109966 = branch1_109393 # MOV operation
branch1_109974 = branch1_109966 # MOV operation
branch1_109978 = (branch1_109974 >> (0x1 & 0x3F)) # SHR operation
branch1_109985 = branch1_109978 # MOV operation
branch1_110289 = branch1_109985 # MOV operation
branch1_110305 = (0xF & branch1_110289) # AND operation
branch1_110876 = branch1_110305 # MOV operation
branch1_110884 = (0x1 | branch1_110876) # OR operation
branch1_111195 = branch1_110884 # MOV operation
branch1_111199 = ((0x40 - branch1_111195) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch1_111207 = branch1_111199 # MOV operation
branch1_111519 = branch1_106407 # MOV operation
branch1_111525 = branch1_111207 # MOV operation
branch1_111527 = branch1_111519 # MOV operation
branch1_111529 = (branch1_111525 & 0xFFFFFFFF) # MOV operation
branch1_111531 = (branch1_111527 >> ((branch1_111529 & 0xFF) & 0x3F)) # SHR operation
branch1_111538 = branch1_111531 # MOV operation
branch1_111824 = branch1_103984 # MOV operation
branch1_111830 = branch1_111538 # MOV operation
branch1_111832 = (branch1_111830 | branch1_111824) # OR operation
branch1_114836 = (((((((((branch1_59734 & 0xFF)) << 8 | (branch1_36638 & 0xFF)) << 8 | (branch1_36639 & 0xFF)) << 8 | (branch1_36640 & 0xFF)) << 8 | (branch1_36641 & 0xFF)) << 8 | (branch1_55037 & 0xFF)) << 8 | (branch1_36643 & 0xFF)) << 8 | (branch1_36644 & 0xFF)) # MOV operation
branch1_117246 = branch1_41997 # MOV operation
branch1_117819 = branch1_117246 # MOV operation
branch1_117827 = branch1_117819 # MOV operation
branch1_117831 = (branch1_117827 >> (0x7 & 0x3F)) # SHR operation
branch1_117838 = branch1_117831 # MOV operation
branch1_120544 = branch1_41997 # MOV operation
branch1_120814 = branch1_120544 # MOV operation
branch1_120830 = branch1_120814 # MOV operation
branch1_120834 = ((branch1_120830 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch1_120841 = branch1_120834 # MOV operation
branch1_121145 = branch1_117838 # MOV operation
branch1_121151 = branch1_120841 # MOV operation
branch1_121153 = (branch1_121151 | branch1_121145) # OR operation
branch1_121465 = branch1_114836 # MOV operation
branch1_121471 = branch1_121153 # MOV operation
branch1_121473 = ((branch1_121471 + branch1_121465) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch1_122075 = branch1_121473 # MOV operation
branch1_122083 = branch1_122075 # MOV operation
branch1_122087 = (branch1_122083 >> (0x2 & 0x3F)) # SHR operation
branch1_122094 = branch1_122087 # MOV operation
branch1_122346 = branch1_122094 # MOV operation
branch1_122362 = (0xF & branch1_122346) # AND operation
branch1_122973 = branch1_122362 # MOV operation
branch1_122981 = (0x1 | branch1_122973) # OR operation
branch1_123304 = branch1_122981 # MOV operation
branch1_123308 = ((0x40 - branch1_123304) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch1_123316 = branch1_123308 # MOV operation
branch1_123602 = branch1_111832 # MOV operation
branch1_123608 = branch1_123316 # MOV operation
branch1_123610 = branch1_123602 # MOV operation
branch1_123612 = (branch1_123608 & 0xFFFFFFFF) # MOV operation
branch1_123614 = (branch1_123610 >> ((branch1_123612 & 0xFF) & 0x3F)) # SHR operation
branch1_123621 = branch1_123614 # MOV operation
branch1_123895 = branch1_97018 # MOV operation
branch1_123901 = branch1_123621 # MOV operation
branch1_123903 = (branch1_123901 | branch1_123895) # OR operation
branch1_124220 = branch1_123903 # MOV operation
branch1_124788 = branch1_124220 # MOV operation

branch2_334 = SymVar_0
branch2_349 = branch2_334 # MOV operation
branch2_14284 = branch2_349 # MOV operation
branch2_14836 = branch2_14284 # MOV operation
branch2_14844 = ((0x2A766E54 + branch2_14836) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch2_15154 = branch2_14844 # MOV operation
branch2_15170 = branch2_15154 # MOV operation
branch2_15174 = ((branch2_15170 << (0x5 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch2_15181 = branch2_15174 # MOV operation
branch2_17493 = branch2_349 # MOV operation
branch2_18097 = branch2_17493 # MOV operation
branch2_18105 = ((0x2A766E54 + branch2_18097) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch2_18681 = branch2_18105 # MOV operation
branch2_18689 = branch2_18681 # MOV operation
branch2_18693 = (branch2_18689 >> (0x3B & 0x3F)) # SHR operation
branch2_18700 = branch2_18693 # MOV operation
branch2_19012 = branch2_15181 # MOV operation
branch2_19018 = branch2_18700 # MOV operation
branch2_19020 = (branch2_19018 | branch2_19012) # OR operation
branch2_19285 = branch2_19020 # MOV operation
branch2_19287 = ((branch2_19285 >> 56) & 0xFF) # Byte reference - MOV operation
branch2_19288 = ((branch2_19285 >> 48) & 0xFF) # Byte reference - MOV operation
branch2_19289 = ((branch2_19285 >> 40) & 0xFF) # Byte reference - MOV operation
branch2_19290 = ((branch2_19285 >> 32) & 0xFF) # Byte reference - MOV operation
branch2_19291 = ((branch2_19285 >> 24) & 0xFF) # Byte reference - MOV operation
branch2_19292 = ((branch2_19285 >> 16) & 0xFF) # Byte reference - MOV operation
branch2_19293 = ((branch2_19285 >> 8) & 0xFF) # Byte reference - MOV operation
branch2_19294 = (branch2_19285 & 0xFF) # Byte reference - MOV operation
branch2_23773 = branch2_349 # MOV operation
branch2_26470 = branch2_19285 # MOV operation
branch2_26756 = branch2_26470 # MOV operation
branch2_26784 = (((0x0) << 64 | branch2_26756) / (((((((((0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x5 & 0xFF))) # DIV operation
branch2_27045 = branch2_23773 # MOV operation
branch2_27051 = branch2_26784 # MOV operation
branch2_27053 = ((branch2_27051 + branch2_27045) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch2_27355 = branch2_27053 # MOV operation
branch2_31854 = branch2_349 # MOV operation
branch2_32432 = branch2_31854 # MOV operation
branch2_32440 = branch2_32432 # MOV operation
branch2_32442 = ((branch2_32440 - 0x18E8E014) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch2_32450 = branch2_32442 # MOV operation
branch2_35140 = branch2_19285 # MOV operation
branch2_35743 = branch2_35140 # MOV operation
branch2_35751 = ((0xB70D976 + branch2_35743) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch2_36037 = branch2_35751 # MOV operation
branch2_36039 = ((branch2_36037 + 0x2E281C99) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch2_36357 = branch2_32450 # MOV operation
branch2_36363 = branch2_36039 # MOV operation
branch2_36365 = branch2_36357 # MOV operation
branch2_36367 = ((branch2_36365 - branch2_36363) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch2_36375 = branch2_36367 # MOV operation
branch2_36635 = branch2_36375 # MOV operation
branch2_36637 = ((branch2_36635 >> 56) & 0xFF) # Byte reference - MOV operation
branch2_36638 = ((branch2_36635 >> 48) & 0xFF) # Byte reference - MOV operation
branch2_36639 = ((branch2_36635 >> 40) & 0xFF) # Byte reference - MOV operation
branch2_36640 = ((branch2_36635 >> 32) & 0xFF) # Byte reference - MOV operation
branch2_36641 = ((branch2_36635 >> 24) & 0xFF) # Byte reference - MOV operation
branch2_36642 = ((branch2_36635 >> 16) & 0xFF) # Byte reference - MOV operation
branch2_36643 = ((branch2_36635 >> 8) & 0xFF) # Byte reference - MOV operation
branch2_36644 = (branch2_36635 & 0xFF) # Byte reference - MOV operation
branch2_41119 = branch2_349 # MOV operation
branch2_41709 = branch2_41119 # MOV operation
branch2_41717 = ((0x3FB85732 + branch2_41709) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch2_41997 = branch2_41717 # MOV operation
branch2_46172 = (branch2_36642 & 0xFF) # MOVZX operation
branch2_46724 = (branch2_46172 & 0xFF) # MOVZX operation
branch2_50883 = (branch2_36637 & 0xFF) # MOVZX operation
branch2_55035 = (branch2_50883 & 0xFF) # MOVZX operation
branch2_55627 = (branch2_46724 & 0xFF) # MOVZX operation
branch2_59732 = (branch2_55627 & 0xFF) # MOVZX operation
branch2_73233 = (((branch2_19293 & 0xFF)) << 8 | (branch2_19294 & 0xFF)) # MOVZX operation
branch2_73469 = (branch2_73233 & 0xFFFF) # MOVZX operation
branch2_81493 = (((branch2_19287 & 0xFF)) << 8 | (branch2_19288 & 0xFF)) # MOVZX operation
branch2_81773 = (branch2_81493 & 0xFFFF) # MOVZX operation
branch2_81775 = (((branch2_81773 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
branch2_81776 = ((branch2_81773 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
branch2_86233 = (branch2_73469 & 0xFFFF) # MOVZX operation
branch2_86521 = (branch2_86233 & 0xFFFF) # MOVZX operation
branch2_86523 = (((branch2_86521 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
branch2_86524 = ((branch2_86521 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
branch2_90638 = (branch2_19289 & 0xFF) # MOVZX operation
branch2_91230 = (branch2_90638 & 0xFF) # MOVZX operation
branch2_95397 = (branch2_19291 & 0xFF) # MOVZX operation
branch2_99528 = (branch2_95397 & 0xFF) # MOVZX operation
branch2_99530 = ((branch2_99528 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch2_100120 = (branch2_91230 & 0xFF) # MOVZX operation
branch2_104225 = (branch2_100120 & 0xFF) # MOVZX operation
branch2_108376 = (branch2_104225 & 0xFF) # MOVZX operation
branch2_108983 = (branch2_108376 & 0xFF) # MOVZX operation
branch2_113112 = (branch2_19292 & 0xFF) # MOVZX operation
branch2_117269 = (branch2_113112 & 0xFF) # MOVZX operation
branch2_117271 = ((branch2_117269 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch2_117831 = (branch2_108983 & 0xFF) # MOVZX operation
branch2_121976 = (branch2_117831 & 0xFF) # MOVZX operation
branch2_121978 = ((branch2_121976 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch2_126143 = (branch2_59732 & 0xFF) # MOVZX operation
branch2_126699 = (branch2_126143 & 0xFF) # MOVZX operation
branch2_130866 = (branch2_55035 & 0xFF) # MOVZX operation
branch2_134971 = (branch2_130866 & 0xFF) # MOVZX operation
branch2_134973 = ((branch2_134971 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch2_135577 = (branch2_126699 & 0xFF) # MOVZX operation
branch2_139729 = (branch2_135577 & 0xFF) # MOVZX operation
branch2_139731 = ((branch2_139729 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch2_143858 = (branch2_36644 & 0xFF) # MOVZX operation
branch2_144426 = (branch2_143858 & 0xFF) # MOVZX operation
branch2_148577 = (branch2_36638 & 0xFF) # MOVZX operation
branch2_152722 = (branch2_148577 & 0xFF) # MOVZX operation
branch2_152724 = ((branch2_152722 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch2_153326 = (branch2_144426 & 0xFF) # MOVZX operation
branch2_157445 = (branch2_153326 & 0xFF) # MOVZX operation
branch2_157447 = ((branch2_157445 & 0xFF) & 0xFF) # Byte reference - MOV operation
branch2_162500 = (((((((((branch2_134973 & 0xFF)) << 8 | (branch2_157447 & 0xFF)) << 8 | (branch2_36639 & 0xFF)) << 8 | (branch2_36640 & 0xFF)) << 8 | (branch2_36641 & 0xFF)) << 8 | (branch2_139731 & 0xFF)) << 8 | (branch2_36643 & 0xFF)) << 8 | (branch2_152724 & 0xFF)) # MOV operation
branch2_164913 = branch2_41997 # MOV operation
branch2_165491 = branch2_164913 # MOV operation
branch2_165499 = branch2_165491 # MOV operation
branch2_165503 = (branch2_165499 >> (0x7 & 0x3F)) # SHR operation
branch2_165510 = branch2_165503 # MOV operation
branch2_168213 = branch2_41997 # MOV operation
branch2_168499 = branch2_168213 # MOV operation
branch2_168515 = branch2_168499 # MOV operation
branch2_168519 = ((branch2_168515 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch2_168526 = branch2_168519 # MOV operation
branch2_168812 = branch2_165510 # MOV operation
branch2_168818 = branch2_168526 # MOV operation
branch2_168820 = (branch2_168818 | branch2_168812) # OR operation
branch2_169099 = branch2_162500 # MOV operation
branch2_169105 = branch2_168820 # MOV operation
branch2_169107 = ((branch2_169105 + branch2_169099) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch2_169695 = branch2_169107 # MOV operation
branch2_169703 = branch2_169695 # MOV operation
branch2_169707 = (branch2_169703 >> (0x2 & 0x3F)) # SHR operation
branch2_169714 = branch2_169707 # MOV operation
branch2_170002 = branch2_169714 # MOV operation
branch2_170018 = (0xF & branch2_170002) # AND operation
branch2_170644 = branch2_170018 # MOV operation
branch2_170652 = (0x1 | branch2_170644) # OR operation
branch2_173377 = branch2_27355 # MOV operation
branch2_173925 = branch2_173377 # MOV operation
branch2_173933 = branch2_173925 # MOV operation
branch2_173937 = (branch2_173933 >> (0x1 & 0x3F)) # SHR operation
branch2_173944 = branch2_173937 # MOV operation
branch2_174240 = branch2_173944 # MOV operation
branch2_174256 = (0xF & branch2_174240) # AND operation
branch2_174852 = branch2_174256 # MOV operation
branch2_174860 = (0x1 | branch2_174852) # OR operation
branch2_177301 = (((((((((branch2_86523 & 0xFF)) << 8 | (branch2_86524 & 0xFF)) << 8 | (branch2_99530 & 0xFF)) << 8 | (branch2_19290 & 0xFF)) << 8 | (branch2_117271 & 0xFF)) << 8 | (branch2_121978 & 0xFF)) << 8 | (branch2_81775 & 0xFF)) << 8 | (branch2_81776 & 0xFF)) # MOV operation
branch2_177535 = branch2_177301 # MOV operation
branch2_177549 = branch2_174860 # MOV operation
branch2_177551 = branch2_177535 # MOV operation
branch2_177553 = (branch2_177549 & 0xFFFFFFFF) # MOV operation
branch2_177555 = ((branch2_177551 << ((branch2_177553 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch2_177562 = branch2_177555 # MOV operation
branch2_179995 = (((((((((branch2_86523 & 0xFF)) << 8 | (branch2_86524 & 0xFF)) << 8 | (branch2_99530 & 0xFF)) << 8 | (branch2_19290 & 0xFF)) << 8 | (branch2_117271 & 0xFF)) << 8 | (branch2_121978 & 0xFF)) << 8 | (branch2_81775 & 0xFF)) << 8 | (branch2_81776 & 0xFF)) # MOV operation
branch2_183018 = branch2_27355 # MOV operation
branch2_183566 = branch2_183018 # MOV operation
branch2_183574 = branch2_183566 # MOV operation
branch2_183578 = (branch2_183574 >> (0x1 & 0x3F)) # SHR operation
branch2_183585 = branch2_183578 # MOV operation
branch2_183877 = branch2_183585 # MOV operation
branch2_183893 = (0xF & branch2_183877) # AND operation
branch2_184506 = branch2_183893 # MOV operation
branch2_184514 = (0x1 | branch2_184506) # OR operation
branch2_184799 = branch2_184514 # MOV operation
branch2_184803 = ((0x40 - branch2_184799) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch2_184811 = branch2_184803 # MOV operation
branch2_185123 = branch2_179995 # MOV operation
branch2_185129 = branch2_184811 # MOV operation
branch2_185131 = branch2_185123 # MOV operation
branch2_185133 = (branch2_185129 & 0xFFFFFFFF) # MOV operation
branch2_185135 = (branch2_185131 >> ((branch2_185133 & 0xFF) & 0x3F)) # SHR operation
branch2_185142 = branch2_185135 # MOV operation
branch2_185402 = branch2_177562 # MOV operation
branch2_185408 = branch2_185142 # MOV operation
branch2_185410 = (branch2_185408 | branch2_185402) # OR operation
branch2_185703 = branch2_185410 # MOV operation
branch2_185717 = branch2_170652 # MOV operation
branch2_185719 = branch2_185703 # MOV operation
branch2_185721 = (branch2_185717 & 0xFFFFFFFF) # MOV operation
branch2_185723 = ((branch2_185719 << ((branch2_185721 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch2_185730 = branch2_185723 # MOV operation
branch2_188475 = branch2_27355 # MOV operation
branch2_189053 = branch2_188475 # MOV operation
branch2_189061 = branch2_189053 # MOV operation
branch2_189065 = (branch2_189061 >> (0x1 & 0x3F)) # SHR operation
branch2_189072 = branch2_189065 # MOV operation
branch2_189324 = branch2_189072 # MOV operation
branch2_189340 = (0xF & branch2_189324) # AND operation
branch2_189955 = branch2_189340 # MOV operation
branch2_189963 = (0x1 | branch2_189955) # OR operation
branch2_192399 = (((((((((branch2_86523 & 0xFF)) << 8 | (branch2_86524 & 0xFF)) << 8 | (branch2_99530 & 0xFF)) << 8 | (branch2_19290 & 0xFF)) << 8 | (branch2_117271 & 0xFF)) << 8 | (branch2_121978 & 0xFF)) << 8 | (branch2_81775 & 0xFF)) << 8 | (branch2_81776 & 0xFF)) # MOV operation
branch2_192647 = branch2_192399 # MOV operation
branch2_192661 = branch2_189963 # MOV operation
branch2_192663 = branch2_192647 # MOV operation
branch2_192665 = (branch2_192661 & 0xFFFFFFFF) # MOV operation
branch2_192667 = ((branch2_192663 << ((branch2_192665 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch2_192674 = branch2_192667 # MOV operation
branch2_195083 = (((((((((branch2_86523 & 0xFF)) << 8 | (branch2_86524 & 0xFF)) << 8 | (branch2_99530 & 0xFF)) << 8 | (branch2_19290 & 0xFF)) << 8 | (branch2_117271 & 0xFF)) << 8 | (branch2_121978 & 0xFF)) << 8 | (branch2_81775 & 0xFF)) << 8 | (branch2_81776 & 0xFF)) # MOV operation
branch2_198116 = branch2_27355 # MOV operation
branch2_198694 = branch2_198116 # MOV operation
branch2_198702 = branch2_198694 # MOV operation
branch2_198706 = (branch2_198702 >> (0x1 & 0x3F)) # SHR operation
branch2_198713 = branch2_198706 # MOV operation
branch2_198965 = branch2_198713 # MOV operation
branch2_198981 = (0xF & branch2_198965) # AND operation
branch2_199592 = branch2_198981 # MOV operation
branch2_199600 = (0x1 | branch2_199592) # OR operation
branch2_199923 = branch2_199600 # MOV operation
branch2_199927 = ((0x40 - branch2_199923) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch2_199935 = branch2_199927 # MOV operation
branch2_200221 = branch2_195083 # MOV operation
branch2_200227 = branch2_199935 # MOV operation
branch2_200229 = branch2_200221 # MOV operation
branch2_200231 = (branch2_200227 & 0xFFFFFFFF) # MOV operation
branch2_200233 = (branch2_200229 >> ((branch2_200231 & 0xFF) & 0x3F)) # SHR operation
branch2_200240 = branch2_200233 # MOV operation
branch2_200514 = branch2_192674 # MOV operation
branch2_200520 = branch2_200240 # MOV operation
branch2_200522 = (branch2_200520 | branch2_200514) # OR operation
branch2_203552 = (((((((((branch2_134973 & 0xFF)) << 8 | (branch2_157447 & 0xFF)) << 8 | (branch2_36639 & 0xFF)) << 8 | (branch2_36640 & 0xFF)) << 8 | (branch2_36641 & 0xFF)) << 8 | (branch2_139731 & 0xFF)) << 8 | (branch2_36643 & 0xFF)) << 8 | (branch2_152724 & 0xFF)) # MOV operation
branch2_205969 = branch2_41997 # MOV operation
branch2_206547 = branch2_205969 # MOV operation
branch2_206555 = branch2_206547 # MOV operation
branch2_206559 = (branch2_206555 >> (0x7 & 0x3F)) # SHR operation
branch2_206566 = branch2_206559 # MOV operation
branch2_209256 = branch2_41997 # MOV operation
branch2_209534 = branch2_209256 # MOV operation
branch2_209550 = branch2_209534 # MOV operation
branch2_209554 = ((branch2_209550 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
branch2_209561 = branch2_209554 # MOV operation
branch2_209868 = branch2_206566 # MOV operation
branch2_209874 = branch2_209561 # MOV operation
branch2_209876 = (branch2_209874 | branch2_209868) # OR operation
branch2_210155 = branch2_203552 # MOV operation
branch2_210161 = branch2_209876 # MOV operation
branch2_210163 = ((branch2_210161 + branch2_210155) & 0xFFFFFFFFFFFFFFFF) # ADD operation
branch2_210751 = branch2_210163 # MOV operation
branch2_210759 = branch2_210751 # MOV operation
branch2_210763 = (branch2_210759 >> (0x2 & 0x3F)) # SHR operation
branch2_210770 = branch2_210763 # MOV operation
branch2_211058 = branch2_210770 # MOV operation
branch2_211074 = (0xF & branch2_211058) # AND operation
branch2_211701 = branch2_211074 # MOV operation
branch2_211709 = (0x1 | branch2_211701) # OR operation
branch2_212006 = branch2_211709 # MOV operation
branch2_212010 = ((0x40 - branch2_212006) & 0xFFFFFFFFFFFFFFFF) # SUB operation
branch2_212018 = branch2_212010 # MOV operation
branch2_212292 = branch2_200522 # MOV operation
branch2_212298 = branch2_212018 # MOV operation
branch2_212300 = branch2_212292 # MOV operation
branch2_212302 = (branch2_212298 & 0xFFFFFFFF) # MOV operation
branch2_212304 = (branch2_212300 >> ((branch2_212302 & 0xFF) & 0x3F)) # SHR operation
branch2_212311 = branch2_212304 # MOV operation
branch2_212623 = branch2_185730 # MOV operation
branch2_212629 = branch2_212311 # MOV operation
branch2_212631 = (branch2_212629 | branch2_212623) # OR operation
branch2_212896 = branch2_212631 # MOV operation
branch2_213508 = branch2_212896 # MOV operation

s.add(z3.If((guard_68738 & 0x1) == 0x1, branch1_124788, branch2_213508) == int(sys.argv[1]))

collisions = 0
while s.check() == z3.sat and collisions < 10:
    print s.model()
    s.add(SymVar_0 != s.model()[SymVar_0])
    collisions += 1

