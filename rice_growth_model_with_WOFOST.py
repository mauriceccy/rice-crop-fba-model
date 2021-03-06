import sys
import scobra
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def Growth():

    m = scobra.Model('Os2384_MO.xls')
    tx = {i:(0,0) for i in m.Reactions() if '_tx' in i}
    biomass = {i:(0,0) for i in m.Reactions() if '_biomass' in i}
    
    m.SetConstraints(tx)
    m.SetConstraints(biomass)
    


    

    #inputs - outputs
        
    inout = {
        
        "Photon_tx_Leaf_Light":(0,None), 
        
        'CO2_tx_Leaf_Light':(None,None),
        'O2_tx_Leaf_Light':(None,None),
        'CO2_tx_Stem_Light':(None,None),
        'O2_tx_Stem_Light':(None,None),
        'CO2_tx_Seed_Light':(None,None),
        'O2_tx_Seed_Light':(None,None),
        
        'CO2_tx_Leaf_Dark':(None,None),
        'O2_tx_Leaf_Dark':(None,None),
        'CO2_tx_Stem_Dark':(None,None),
        'O2_tx_Stem_Dark':(None,None),
        'CO2_tx_Seed_Dark':(None,None),
        'O2_tx_Seed_Dark':(None,None),

        'WATER_tx_Leaf_Light':(None,None),
        'PROTON_tx_Leaf_Light':(None,None),
        'WATER_tx_Stem_Light':(None,None),
        'PROTON_tx_Stem_Light':(None,None),
        'WATER_tx_Seed_Light':(None,None),
        'PROTON_tx_Seed_Light':(None,None),

        'WATER_tx_Leaf_Dark':(None,None),
        'PROTON_tx_Leaf_Dark':(None,None),
        'WATER_tx_Stem_Dark':(None,None),
        'PROTON_tx_Stem_Dark':(None,None),
        'WATER_tx_Seed_Dark':(None,None),
        'PROTON_tx_Seed_Dark':(None,None),        


                        
        'NO3_tx_CP_Light':(0,None),
        'NH3_tx_CP_Light':(0,None),
        'SO4_tx_CP_Light':(0,None),
        'PHOSPHATE_tx_CP_Light':(0,None),
        'Mg_tx_CP_Light':(0,None),
        
        'NO3_tx_CP_Dark':(0,None),
        'NH3_tx_CP_Dark':(0,None),
        'SO4_tx_CP_Dark':(0,None),
        'PHOSPHATE_tx_CP_Dark':(0,None),
        'Mg_tx_CP_Dark':(0,None),


        'NADPH_Dehydrogenase_p_Leaf_Light':(0,0),
        'Plastoquinol_Oxidase_p_Leaf_Light':(0,0),
        'NADPH_Dehydrogenase_p_Stem_Light':(0,0),
        'Plastoquinol_Oxidase_p_Stem_Light':(0,0),
        'NADPH_Dehydrogenase_p_Seed_Light':(0,0),
        'Plastoquinol_Oxidase_p_Seed_Light':(0,0),

        'NADPH_Dehydrogenase_p_Leaf_Dark':(0,0),
        'Plastoquinol_Oxidase_p_Leaf_Dark':(0,0),
        'NADPH_Dehydrogenase_p_Stem_Dark':(0,0),
        'Plastoquinol_Oxidase_p_Stem_Dark':(0,0),
        'NADPH_Dehydrogenase_p_Seed_Dark':(0,0),
        'Plastoquinol_Oxidase_p_Seed_Dark':(0,0),


        }

    m.SetConstraints(inout)

    #maintenance
    
    maintain = ['NADPHOxid_c_tx_Seed_Light','NADPHOxid_m_tx_Seed_Light','NADPHOxid_p_tx_Seed_Light','NADPHOxid_x_tx_Seed_Light',
               'NADPHOxid_c_tx_Leaf_Light','NADPHOxid_m_tx_Leaf_Light','NADPHOxid_p_tx_Leaf_Light','NADPHOxid_x_tx_Leaf_Light',
               'NADPHOxid_c_tx_Stem_Light','NADPHOxid_m_tx_Stem_Light','NADPHOxid_p_tx_Stem_Light','NADPHOxid_x_tx_Stem_Light',
               'ATPase_c_tx_Leaf_Light','ATPase_c_tx_Stem_Light','ATPase_c_tx_Seed_Light',

               'NADPHOxid_c_tx_Seed_Dark','NADPHOxid_m_tx_Seed_Dark','NADPHOxid_p_tx_Seed_Dark','NADPHOxid_x_tx_Seed_Dark',
               'NADPHOxid_c_tx_Leaf_Dark','NADPHOxid_m_tx_Leaf_Dark','NADPHOxid_p_tx_Leaf_Dark','NADPHOxid_x_tx_Leaf_Dark',
               'NADPHOxid_c_tx_Stem_Dark','NADPHOxid_m_tx_Stem_Dark','NADPHOxid_p_tx_Stem_Dark','NADPHOxid_x_tx_Stem_Dark',
               'ATPase_c_tx_Leaf_Dark','ATPase_c_tx_Stem_Dark','ATPase_c_tx_Seed_Dark']
    for i in maintain:
        m.SetConstraint(i,0,0)

    
        


    m.SetReacsFixedRatio({'RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_p_Leaf_Light':3, 'RXN-961_p_Leaf_Light':1})
    m.SetReacsFixedRatio({'RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_p_Stem_Light':3, 'RXN-961_p_Stem_Light':1})
    m.SetReacsFixedRatio({'RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_p_Seed_Light':3, 'RXN-961_p_Seed_Light':1})
    
    m.SetReacsFixedRatio({'RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_p_Leaf_Dark':3, 'RXN-961_p_Leaf_Dark':1})
    m.SetReacsFixedRatio({'RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_p_Stem_Dark':3, 'RXN-961_p_Stem_Dark':1})
    m.SetReacsFixedRatio({'RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN_p_Seed_Dark':3, 'RXN-961_p_Seed_Dark':1})

    sto = ['Starch', 'Sucrose','Glucose','Fructose','Malate','Fumarate','Citrate','Nitrate']

    dns = filter(lambda s: "LightDark_storage" in s,m.Reactions())
    for r in dns:
        if r.split('_')[0] not in sto:
            m.SetConstraint(r,0,None)
    


    from scobra.classes import matrix
    mat = matrix.matrix()
    temp_sol = {'Leaf_Biomass':0,'Stem_Biomass':0,'Seed_Biomass':0}
    leaf_rate,stem_rate,seed_rate = 0,0,0

    seedreac = filter(lambda s: "_Seed" in s, m.Reactions())
    seedcon = m.GetConstraints(seedreac)
    for reac in seedreac:
        m.SetConstraint(reac,0,0)
        
    temp_sol['Leaf_Biomass'] = 0
    temp_sol['Stem_Biomass'] = 0
    temp_sol['Seed_Biomass'] = 0
    
    Pmax = 1000       
    Pmax = (Pmax*60*60*12)*1e-6

    flag_seed = 0
    

    #fr = open('WOFOST_rates_one_plant_stress.csv','r')
    fr = open('WOFOST_rates_one_plant.csv','r')
    for i, val in enumerate(fr):
        if i>0:
            val = val.replace('"','')

            
            rates = val.strip('\n').split(',')
            
            data = float(rates[0])
            day = float(rates[1])
            leaf_rate = float(rates[2])
            stem_rate = float(rates[3])
            seed_rate = float(rates[4])
            
            
            print data, day,leaf_rate,stem_rate,seed_rate
            
            div_rate_day = 0.7
            div_rate_night = 0.3
            if leaf_rate>0:
                m.SetConstraint('Biomass_Leaf_deg_tx_Light',0,0)
                m.SetConstraint('Biomass_Leaf_deg_tx_Dark',0,0)
                
                
                m.SetConstraint('Biomass_Leaf_tx_Light',leaf_rate*div_rate_day,leaf_rate*div_rate_day)
                m.SetConstraint('Biomass_Leaf_tx_Dark',leaf_rate*div_rate_night,leaf_rate*div_rate_night)
                
            else:
                
                

                m.SetConstraint('Biomass_Leaf_deg_tx_Light',leaf_rate*div_rate_day,leaf_rate*div_rate_day)
                m.SetConstraint('Biomass_Leaf_deg_tx_Dark',leaf_rate*div_rate_night,leaf_rate*div_rate_night)
                
                m.SetConstraint('Biomass_Leaf_tx_Light',0,0)
                m.SetConstraint('Biomass_Leaf_tx_Dark',0,0)
                
                m.SetConstraint('NCC_biomass_Leaf_Light',None,0)
                m.SetConstraint('PHYTOL_biomass_Leaf_Light',None,0)
                m.SetConstraint('Mg_biomass_Leaf_Light',None,0)
                m.SetConstraint('SO3_biomass_Leaf_Light',None,0)
                
                m.SetConstraint('NCC_biomass_Leaf_Dark',None,0)
                m.SetConstraint('PHYTOL_biomass_Leaf_Dark',None,0)
                m.SetConstraint('Mg_biomass_Leaf_Dark',None,0)
                m.SetConstraint('SO3_biomass_Leaf_Dark',None,0)

                

                
                
            if stem_rate>0:
                m.SetConstraint('Biomass_Stem_deg_tx_Light',0,0)
                m.SetConstraint('Biomass_Stem_deg_tx_Dark',0,0)
                m.SetConstraint('Biomass_Stem_tx_Light',stem_rate*div_rate_day,stem_rate*div_rate_day)
                m.SetConstraint('Biomass_Stem_tx_Dark',stem_rate*div_rate_night,stem_rate*div_rate_night)
                
            else:
                
                m.SetConstraint('Biomass_Stem_deg_tx_Light',stem_rate*div_rate_day,stem_rate*div_rate_day)
                m.SetConstraint('Biomass_Stem_deg_tx_Dark',stem_rate*div_rate_night,stem_rate*div_rate_night)
                m.SetConstraint('Biomass_Stem_tx_Light',0,0)
                m.SetConstraint('Biomass_Stem_tx_Dark',0,0)

                
            if seed_rate>0:
                if flag_seed == 0:
                    m.SetConstraints(seedcon)
                    flag_seed = 1
                
                m.SetConstraint('Biomass_Seed_tx_Light',seed_rate*div_rate_day,seed_rate*div_rate_day)
                m.SetConstraint('Biomass_Seed_tx_Dark',seed_rate*div_rate_night,seed_rate*div_rate_night)



              


            #######################################################################
                
            M_ATP = 0.00727
            M_NADPH = 0.00256 #mol/day/ 1 g DW biomass

            M_ATP_D_N = 0.003635 # M_ATP/2
            M_NADPH_D_N = 0.00128 #M_NADPH/2
            
            ULM, USTM, USM = temp_sol['Leaf_Biomass'], temp_sol['Stem_Biomass'], temp_sol['Seed_Biomass']
            UpdatedRate = {}

            #### Leaf #####
            UpdatedRate['ATPase_c_tx_Leaf_Light']=( -M_ATP_D_N*ULM , -M_ATP_D_N*ULM )
            UpdatedRate['ATPase_c_tx_Leaf_Dark']=( -M_ATP_D_N*ULM , -M_ATP_D_N*ULM )
            Per_Com_NADPH_D_N = M_NADPH_D_N/3
                
            UpdatedRate['NADPHOxid_c_tx_Leaf_Light']=( -Per_Com_NADPH_D_N*ULM,-Per_Com_NADPH_D_N*ULM)
            UpdatedRate['NADPHOxid_m_tx_Leaf_Light']=( -Per_Com_NADPH_D_N*ULM,-Per_Com_NADPH_D_N*ULM)
            UpdatedRate['NADPHOxid_p_tx_Leaf_Light']=( -Per_Com_NADPH_D_N*ULM,-Per_Com_NADPH_D_N*ULM)
            
            UpdatedRate['NADPHOxid_c_tx_Leaf_Dark']=( -Per_Com_NADPH_D_N*ULM,-Per_Com_NADPH_D_N*ULM)
            UpdatedRate['NADPHOxid_m_tx_Leaf_Dark']=( -Per_Com_NADPH_D_N*ULM,-Per_Com_NADPH_D_N*ULM)
            UpdatedRate['NADPHOxid_p_tx_Leaf_Dark']=( -Per_Com_NADPH_D_N*ULM,-Per_Com_NADPH_D_N*ULM)
            

            #### Stem #####
                
            UpdatedRate['ATPase_c_tx_Stem_Light']=( -M_ATP_D_N*USTM , -M_ATP_D_N*USTM )
            UpdatedRate['ATPase_c_tx_Stem_Dark']=( -M_ATP_D_N*USTM , -M_ATP_D_N*USTM )

            Per_Com_NADPH_D_N = M_NADPH_D_N/3
                
            UpdatedRate['NADPHOxid_c_tx_Stem_Light']=( -Per_Com_NADPH_D_N*USTM,-Per_Com_NADPH_D_N*USTM)
            UpdatedRate['NADPHOxid_m_tx_Stem_Light']=( -Per_Com_NADPH_D_N*USTM,-Per_Com_NADPH_D_N*USTM)
            UpdatedRate['NADPHOxid_p_tx_Stem_Light']=( -Per_Com_NADPH_D_N*USTM,-Per_Com_NADPH_D_N*USTM)

            UpdatedRate['NADPHOxid_c_tx_Stem_Dark']=( -Per_Com_NADPH_D_N*USTM,-Per_Com_NADPH_D_N*USTM)
            UpdatedRate['NADPHOxid_m_tx_Stem_Dark']=( -Per_Com_NADPH_D_N*USTM,-Per_Com_NADPH_D_N*USTM)
            UpdatedRate['NADPHOxid_p_tx_Stem_Dark']=( -Per_Com_NADPH_D_N*USTM,-Per_Com_NADPH_D_N*USTM)

                            
            ##	#### Seed #####
            M_ATP = 0.0001
            M_NADPH = 0.000033 #mol/day/ 1 g DW biomass
            
            M_ATP_D_N = 0.0001/2 # M_ATP/2
            M_NADPH_D_N = 0.000033/2 #M_NADPH/2
            
            UpdatedRate['ATPase_c_tx_Seed_Light']=( -M_ATP_D_N*USM , -M_ATP_D_N*USM )
            UpdatedRate['ATPase_c_tx_Seed_Dark']=( -M_ATP_D_N*USM , -M_ATP_D_N*USM )

            Per_Com_NADPH_D_N = M_NADPH_D_N/3
                
            UpdatedRate['NADPHOxid_c_tx_Seed_Light']=( -Per_Com_NADPH_D_N*USM,-Per_Com_NADPH_D_N*USM)
            UpdatedRate['NADPHOxid_m_tx_Seed_Light']=( -Per_Com_NADPH_D_N*USM,-Per_Com_NADPH_D_N*USM)
            UpdatedRate['NADPHOxid_p_tx_Seed_Light']=( -Per_Com_NADPH_D_N*USM,-Per_Com_NADPH_D_N*USM)

            UpdatedRate['NADPHOxid_c_tx_Seed_Dark']=( -Per_Com_NADPH_D_N*USM,-Per_Com_NADPH_D_N*USM)
            UpdatedRate['NADPHOxid_m_tx_Seed_Dark']=( -Per_Com_NADPH_D_N*USM,-Per_Com_NADPH_D_N*USM)
            UpdatedRate['NADPHOxid_p_tx_Seed_Dark']=( -Per_Com_NADPH_D_N*USM,-Per_Com_NADPH_D_N*USM)


            m.SetConstraints(UpdatedRate)

            
            m.MinFluxSolve()
            
                
            #m.Solve()
            


            sol = m.GetSol()

            sol['Day'] = day       

            



            bioval_all =['Biomass_Leaf_tx_Light','Biomass_Leaf_deg_tx_Light','Biomass_Stem_tx_Light','Biomass_Stem_deg_tx_Light','Biomass_Seed_tx_Light',
                         'Biomass_Leaf_tx_Dark','Biomass_Leaf_deg_tx_Dark','Biomass_Stem_tx_Dark','Biomass_Stem_deg_tx_Dark','Biomass_Seed_tx_Dark']


            
            for item in bioval_all:
                if item not in sol:
                    sol[item] = 0
            
            

            sol['Leaf_Biomass'] = temp_sol['Leaf_Biomass'] + sol['Biomass_Leaf_tx_Light'] + sol['Biomass_Leaf_deg_tx_Light']+ sol['Biomass_Leaf_tx_Dark'] + sol['Biomass_Leaf_deg_tx_Dark']
            temp_sol['Leaf_Biomass'] = sol['Leaf_Biomass']
                

            sol['Stem_Biomass'] = temp_sol['Stem_Biomass']+ sol['Biomass_Stem_tx_Light'] + sol['Biomass_Stem_deg_tx_Light']+ sol['Biomass_Stem_tx_Dark'] + sol['Biomass_Stem_deg_tx_Dark']
            temp_sol['Stem_Biomass'] = sol['Stem_Biomass']


            sol['Seed_Biomass'] = temp_sol['Seed_Biomass']+ sol['Biomass_Seed_tx_Light']+ sol['Biomass_Seed_tx_Dark']
            temp_sol['Seed_Biomass'] = sol['Seed_Biomass']


                
            mat = mat.UpdateFromDic(sol)
            
        
    #fw.close()    
    return mat



