import { logIfUnequal, locale, capFirst, formatFinancialYear, ratingColor } from './utils.js';
import { ContactSection } from './components/contacts.js';
import { TextField } from './components/common.js';
import { AnnualSection, QuarterlySection, OverUnderSection } from './components/indicators.js';
import { AuditOpinions } from './components/audit-opinions.js';
import { ProfileHeader } from './components/profile-header.js';

class ProfilePage {
  constructor() {
    const pageData = JSON.parse(document.getElementById('page-data').textContent);

    new ProfileHeader(pageData.geography, pageData.total_population, pageData.population_density);

    const municipality = {
      code: pageData.geography.geo_code,
      name: pageData.geography.short_name,
    };

    new AnnualSection("#cash-balance", pageData.indicators.cash_at_year_end, municipality);
    new AnnualSection("#cash-coverage", pageData.indicators.cash_coverage, municipality);
    new OverUnderSection("#operating-budget", pageData.indicators.op_budget_diff, municipality);
    new OverUnderSection("#capital-budget", pageData.indicators.cap_budget_diff, municipality);
    new AnnualSection("#repairs-maintenance", pageData.indicators.rep_maint_perc_ppe, municipality);
    new AnnualSection("#wasteful-expenditure", pageData.indicators.wasteful_exp, municipality);
    new QuarterlySection("#current-ratio", pageData.indicators.current_ratio, municipality);
    new QuarterlySection("#liquidity-ratio", pageData.indicators.liquidity_ratio, municipality);
    new QuarterlySection("#collection-rate", pageData.indicators.current_debtors_collection_rate, municipality);
    new AnnualSection("#wages-salaries", pageData.indicators.expenditure_trends_staff, municipality);
    new AnnualSection("#contractor-services", pageData.indicators.expenditure_trends_contracting, municipality);




    new ContactSection(pageData.mayoral_staff);

    new AuditOpinions(pageData.audit_opinions);
  }
}

new ProfilePage();

// Re-initialise webflow interactions so that cloned elements respond to interactions
Webflow.require('ix2').init();
