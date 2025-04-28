# stacking-model-for-phase-kinetics
This project focuses on predicting the formation of the detrimental sigma
phase (σ-phase) in stainless steels, a brittle intermetallic compound that
compromises mechanical integrity and corrosion resistance, particularly when
alloys are exposed to temperatures between 600–900 °C. The primary objective
was to develop a predictive model for the onset time of sigma phase formation by
analyzing the influence of temperature, time, and elemental composition,
including trace elements, using machine learning techniques.The methodology
involved collecting data from existing research, preprocessing it through
techniques like imputation and normalization, and employing feature selection
methods. A key aspect was integrating experimental data with theoretical
calculations derived from Density Functional Theory (DFT) to compute
formation enthalpies and using Classical Nucleation Theory (CNT) concepts to
engineer features representing kinetic factors. An ensemble machine learning
model, specifically stacking using Random Forest Regression, was developed to
combine these different data sources and predict the logarithm of the onset time.
The final model achieved an R² score of 0.64, demonstrating reasonable
predictive capability. Feature importance analysis identified Molybdenum (Mo)
and Aluminium (Al) as the most significant elements influencing sigma phase
formation, with other elements like Silicon (Si), Nickel (Ni), Tungsten (W),
Carbon (C), Nitrogen (N), and Copper (Cu) also contributing. The study
confirmed the accelerating effect of higher temperatures on sigma phase
formation. This research provides a data-driven approach that integrates machine
learning with metallurgical principles (DFT, CNT) to enhance the prediction of
sigma phase transformation. The resulting insights can aid in optimizing steel
compositions and heat treatment processes to mitigate sigma phase embrittlement
and improve the performance of stainless steels in various industrial applications.
