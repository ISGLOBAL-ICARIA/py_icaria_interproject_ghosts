all_forms_redcap = [
    'screening','id','vaccination_history','clinical_history' ,'unscheduled',
    'household_follow_up','mortality_surveillance','drug_reaction','intervention',
    'socioeconomics','noncompliant','migration','unscheduled','ae','sae',
    'withdrawal', 'death', 'cohort_clinical_history', 'cohort_tests', 'vacc_card',
    'macrolide_resistance_baseline','macrolide_resistance_t2',
    'macrolide_resistance_t3', 'azi_interactions_with_epi_vaccines'
]

prefix_three = [
    "HF01.01","HF01.02","HF01.03","HF02.01","HF02.02","HF03","HF04.01",
    "HF04.02","HF05.01","HF05.02","HF06","HF08.01","HF08.02","HF08.03","HF08.04"
]

dict_prefixes = {
    "HF01.01":"101",
    "HF01.02":"102",
    "HF01.03":"103",
    "HF02.01":"201",
    "HF02.02":"202",
    "HF03": "301",
    "HF04.01":"401",
    "HF04.02":"402",
    "HF05.01":"501",
    "HF05.02":"502",
    "HF06": "601",
    "HF08.01":"801",
    "HF08.02":"802",
    "HF08.03":"803",
    "HF08.04":"804",
    "HF10": "1001",
    "HF11.01":"1101",
    "HF11.02":"1102",
    "HF12.01":"1201",
    "HF12.02":"1202",
    "HF13.01":"1301",
    "HF13.02":"1302",
    "HF15": "1501",
    "HF16.01":"1601",
    "HF16.02":"1602",
    "HF16.03":"1603",
    "HF16.04":"1604",
    "HF16.05":"1605",
    "HF17.01":"1701",
    "HF17.02":"1702"
}

complete_fields = [
    'screening_complete',
    'id_complete',
    'vaccination_history_complete',
    'clinical_history_complete',
    'household_follow_up_complete',
    'drug_reaction_complete',
    'intervention_complete',
    'socioeconomics_complete',
    'noncompliant_complete',
    'migration_complete',
    'ae_complete',
    'sae_complete',
    'withdrawal_complete',
    'death_complete',
    'cohort_clinical_history_complete',
    'cohort_tests_complete',
    'mortality_surveillance_c175_complete',
    'macrolide_resistance_baseline_complete',
    'macrolide_resistance_t2_complete',
    'macrolide_resistance_t3_complete',
    'azi_interactions_with_epi_vaccines_complete',
    'rtss_complete',
    'unscheduled_complete',
]

interv_fields = [
    'screening_interviewer_id',
    'id_interviewer_id',
    'his_interviewer_id',
    'clin_interviewer_id',
    'hh_interviewer_id',
    'react_interviewer_id',
    'int_interviewer_id',
    'se_interviewer_id',
    'comp_interviewer_id',
    'mig_interviewer_id',
    'ae_interviewer_id',
    'sae_interviewer_id',
    'wdrawal_interviewer_id',
    'death_interviewer_id',
    'ch_his_interviewer_id',
    'ch_rdt_interviewer_id',
    'ms_interviewer_id',
    'mrs_interviewer_id',
    'mrs_interviewer_id_t2',
    'mrs_interviewer_id_t3',
    'azivac_interviewer_id',
    'rtss_interviewer_id',
    'unsch_interviewer_id'
]


fields_per_event = {
    'epipenta1_v0_recru_arm_1': ['screening_interviewer_id','screening_complete', 'id_interviewer_id','id_complete','his_interviewer_id','vaccination_history_complete','int_interviewer_id','intervention_complete','se_interviewer_id','socioeconomics_complete','mrs_interviewer_id', 'macrolide_resistance_baseline_complete'],
    'epipenta2_v1_iptis_arm_1': ['clin_interviewer_id','clinical_history_complete','int_interviewer_id','intervention_complete'],
    'epipenta3_v2_iptis_arm_1': ['clin_interviewer_id','clinical_history_complete','int_interviewer_id','intervention_complete','mrs_interviewer_id_t2', 'macrolide_resistance_t2_complete'],
    'epivita_v3_iptisp3_arm_1': ['clin_interviewer_id','clinical_history_complete','int_interviewer_id','intervention_complete'],
    'epimvr1_v4_iptisp4_arm_1': ['clin_interviewer_id','clinical_history_complete','int_interviewer_id','intervention_complete','azivac_interviewer_id', 'azi_interactions_with_epi_vaccines_complete'],
    'epivita_v5_iptisp5_arm_1': ['clin_interviewer_id','clinical_history_complete','int_interviewer_id','intervention_complete','azivac_interviewer_id', 'azi_interactions_with_epi_vaccines_complete'],
    'epimvr2_v6_iptisp6_arm_1': ['clin_interviewer_id','clinical_history_complete','int_interviewer_id','intervention_complete'],
    'hhafter_1st_dose_o_arm_1': ['hh_interviewer_id','household_follow_up_complete','react_interviewer_id','drug_reaction_complete','se_interviewer_id','socioeconomics_complete'],
    'cohort_after_mrv_2_arm_1': ['ch_his_interviewer_id', 'cohort_clinical_history_complete','ch_rdt_interviewer_id', 'cohort_tests_complete'],
    'hhat_18th_month_of_arm_1': ['hh_interviewer_id','household_follow_up_complete','int_interviewer_id','intervention_complete','mrs_interviewer_id_t3', 'macrolide_resistance_t3_complete'],
    'rtss_arm_1': ['rtss_interviewer_id','rtss_complete'],
    'adverse_events_arm_1': ['ae_interviewr_id','ae_complete','sae_interviewer_id', 'sae_complete'],
    'out_of_schedule_arm_1': ['comp_interviewer_id','noncompliant_complete','mig_interviewer_id', 'migration_complete','unsch_interviewer_id','unscheduled_complete','mortality_surveillance_c175_complete', 'ms_interviewer_id'],
    'end_of_fu_arm_1': ['wdrawal_interviewer_id', 'withdrawal_complete','death_interviewer_id', 'death_complete']
}