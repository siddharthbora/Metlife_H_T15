#!/usr/bin/env python3
"""
MetLife Professional Test Monitoring Dashboard
============================================

A professional-grade monitoring dashboard with industry-standard UI design,
inspired by leading monitoring tools like Grafana, Datadog, and New Relic.

Features:
- Professional, clean UI design
- Industry-standard metrics and visualizations
- Comprehensive monitoring capabilities
- Single unified dashboard for all test data
- Executive-ready reporting
- Mobile-responsive design

Author: MetLife Automation Team
Version: 3.0.0 - Professional Edition
"""

import os
import sys
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path
import argparse
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from collections import defaultdict, Counter
import statistics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('professional_dashboard.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class DashboardMetrics:
    """Professional dashboard metrics"""
    total_tests: int
    passed_tests: int
    failed_tests: int
    skipped_tests: int
    pass_rate: float
    failure_rate: float
    avg_execution_time: float
    total_execution_time: float
    test_suites: int
    critical_failures: int
    flaky_tests: int
    performance_issues: int
    system_health: float
    reliability_score: float
    last_execution: str

class ProfessionalDashboardParser:
    """Parser for Robot Framework XML files with professional metrics"""
    
    def __init__(self):
        self.all_data = []
        
    def parse_all_xml_files(self, root_dir: str = ".") -> Dict:
        """Parse all XML files and generate professional metrics"""
        logger.info(f"Scanning for test results in: {root_dir}")
        
        xml_files = self._find_all_xml_files(root_dir)
        logger.info(f"Found {len(xml_files)} test result files")
        
        all_suites = []
        all_tests = []
        
        for xml_file in xml_files:
            try:
                data = self._parse_xml_file(xml_file)
                if data:
                    all_suites.extend(data['suites'])
                    all_tests.extend(data['tests'])
            except Exception as e:
                logger.warning(f"Skipped {xml_file}: {e}")
        
        # Calculate professional metrics
        metrics = self._calculate_metrics(all_tests, all_suites)
        
        # Generate visualizations data
        charts_data = self._prepare_charts_data(all_tests, all_suites)
        
        # Generate insights
        insights = self._generate_insights(all_tests, all_suites, metrics)
        
        return {
            'metrics': metrics,
            'suites': all_suites,
            'tests': all_tests,
            'charts': charts_data,
            'insights': insights,
            'timestamp': datetime.now().isoformat()
        }
    
    def _find_all_xml_files(self, root_dir: str) -> List[str]:
        """Find all output.xml files"""
        xml_files = []
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file == 'output.xml':
                    xml_files.append(os.path.join(root, file))
        return xml_files
    
    def _parse_xml_file(self, xml_file: str) -> Dict:
        """Parse single XML file"""
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        suites = []
        tests = []
        
        for suite_elem in root.findall('.//suite'):
            suite_data = self._parse_suite(suite_elem, xml_file)
            if suite_data:
                suites.append(suite_data)
                tests.extend(suite_data['tests'])
        
        return {'suites': suites, 'tests': tests}
    
    def _parse_suite(self, suite_elem, source_file: str) -> Dict:
        """Parse test suite"""
        suite_name = suite_elem.get('name', '')
        status_elem = suite_elem.find('status')
        
        if status_elem is not None:
            status = status_elem.get('status', 'PASS')
            start_time = status_elem.get('start', '')
            elapsed = float(status_elem.get('elapsed', 0)) / 1000.0
        else:
            status = 'PASS'
            start_time = ''
            elapsed = 0.0
        
        tests = []
        for test_elem in suite_elem.findall('test'):
            test_data = self._parse_test(test_elem, suite_name)
            if test_data:
                tests.append(test_data)
        
        passed = sum(1 for t in tests if t['status'] == 'PASS')
        failed = sum(1 for t in tests if t['status'] == 'FAIL')
        
        return {
            'name': suite_name,
            'status': status,
            'start_time': start_time,
            'elapsed_time': elapsed,
            'tests': tests,
            'passed': passed,
            'failed': failed,
            'total': len(tests),
            'pass_rate': (passed / len(tests) * 100) if tests else 100,
            'source': source_file
        }
    
    def _parse_test(self, test_elem, suite_name: str) -> Dict:
        """Parse test case"""
        test_name = test_elem.get('name', '')
        status_elem = test_elem.find('status')
        
        if status_elem is not None:
            status = status_elem.get('status', 'PASS')
            start_time = status_elem.get('start', '')
            elapsed = float(status_elem.get('elapsed', 0)) / 1000.0
            error = status_elem.text if status_elem.text else ""
        else:
            status = 'PASS'
            start_time = ''
            elapsed = 0.0
            error = ""
        
        tags = [tag.text for tag in test_elem.findall('tag') if tag.text]
        doc_elem = test_elem.find('doc')
        doc = doc_elem.text if doc_elem is not None else ""
        
        return {
            'name': test_name,
            'suite': suite_name,
            'status': status,
            'start_time': start_time,
            'elapsed_time': elapsed,
            'error': error,
            'tags': tags,
            'doc': doc,
            'critical': 'critical' in tags or 'smoke' in tags
        }
    
    def _calculate_metrics(self, all_tests: List[Dict], all_suites: List[Dict]) -> DashboardMetrics:
        """Calculate professional dashboard metrics"""
        if not all_tests:
            return DashboardMetrics(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, "N/A")
        
        total = len(all_tests)
        passed = sum(1 for t in all_tests if t['status'] == 'PASS')
        failed = sum(1 for t in all_tests if t['status'] == 'FAIL')
        skipped = total - passed - failed
        
        pass_rate = (passed / total * 100) if total > 0 else 0
        failure_rate = (failed / total * 100) if total > 0 else 0
        
        times = [t['elapsed_time'] for t in all_tests]
        avg_time = statistics.mean(times) if times else 0
        total_time = sum(times)
        
        critical_failures = sum(1 for t in all_tests if t['status'] == 'FAIL' and t['critical'])
        
        # Detect flaky tests (timeout/connection errors)
        flaky = sum(1 for t in all_tests if any(word in t['error'].lower() 
                    for word in ['timeout', 'connection', 'intermittent']))
        
        # Performance issues (tests taking > 2x average)
        perf_issues = sum(1 for t in all_tests if t['elapsed_time'] > avg_time * 2)
        
        # System health score
        health = pass_rate * 0.7 + (100 - (critical_failures / total * 100)) * 0.3
        
        # Reliability score
        reliability = 100 - (flaky / total * 100) if total > 0 else 100
        
        last_exec = max([t['start_time'] for t in all_tests]) if all_tests else "N/A"
        
        return DashboardMetrics(
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed,
            skipped_tests=skipped,
            pass_rate=pass_rate,
            failure_rate=failure_rate,
            avg_execution_time=avg_time,
            total_execution_time=total_time,
            test_suites=len(all_suites),
            critical_failures=critical_failures,
            flaky_tests=flaky,
            performance_issues=perf_issues,
            system_health=health,
            reliability_score=reliability,
            last_execution=last_exec
        )
    
    def _prepare_charts_data(self, all_tests: List[Dict], all_suites: List[Dict]) -> Dict:
        """Prepare data for professional charts"""
        
        # Pass/Fail distribution
        status_dist = Counter([t['status'] for t in all_tests])
        
        # Suite performance
        suite_perf = [(s['name'], s['elapsed_time'], s['pass_rate']) for s in all_suites]
        
        # Execution time distribution
        time_buckets = {'<1s': 0, '1-5s': 0, '5-15s': 0, '15-30s': 0, '>30s': 0}
        for t in all_tests:
            time = t['elapsed_time']
            if time < 1:
                time_buckets['<1s'] += 1
            elif time < 5:
                time_buckets['1-5s'] += 1
            elif time < 15:
                time_buckets['5-15s'] += 1
            elif time < 30:
                time_buckets['15-30s'] += 1
            else:
                time_buckets['>30s'] += 1
        
        # Tag distribution
        all_tags = [tag for t in all_tests for tag in t['tags']]
        tag_dist = dict(Counter(all_tags).most_common(10))
        
        # Timeline data
        timeline = []
        for suite in all_suites:
            timeline.append({
                'time': suite['start_time'],
                'suite': suite['name'],
                'pass_rate': suite['pass_rate'],
                'duration': suite['elapsed_time']
            })
        
        return {
            'status_distribution': dict(status_dist),
            'suite_performance': suite_perf,
            'time_distribution': time_buckets,
            'tag_distribution': tag_dist,
            'timeline': timeline
        }
    
    def _generate_insights(self, all_tests: List[Dict], all_suites: List[Dict], metrics: DashboardMetrics) -> List[Dict]:
        """Generate actionable insights"""
        insights = []
        
        # Health insights
        if metrics.system_health < 80:
            insights.append({
                'type': 'warning',
                'title': 'System Health Below Target',
                'message': f'Current health score is {metrics.system_health:.1f}%. Target is 80%+',
                'action': 'Review failed tests and address critical issues'
            })
        
        # Performance insights
        if metrics.performance_issues > 0:
            insights.append({
                'type': 'info',
                'title': 'Performance Optimization Opportunity',
                'message': f'{metrics.performance_issues} tests are taking longer than expected',
                'action': 'Optimize slow-running tests to improve overall execution time'
            })
        
        # Reliability insights
        if metrics.flaky_tests > 0:
            insights.append({
                'type': 'warning',
                'title': 'Test Stability Issues Detected',
                'message': f'{metrics.flaky_tests} tests showing flaky behavior',
                'action': 'Investigate and stabilize intermittent test failures'
            })
        
        # Success insights
        if metrics.pass_rate >= 95:
            insights.append({
                'type': 'success',
                'title': 'Excellent Test Performance',
                'message': f'Pass rate of {metrics.pass_rate:.1f}% exceeds target',
                'action': 'Maintain current quality standards'
            })
        
        return insights

class ProfessionalDashboardGenerator:
    """Generate professional-grade HTML dashboard"""
    
    def generate(self, data: Dict, output_path: str = "professional_dashboard.html"):
        """Generate professional dashboard HTML"""
        logger.info(f"Generating professional dashboard: {output_path}")
        
        html = self._generate_html(data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        logger.info(f"Professional dashboard generated: {output_path}")
        return output_path
    
    def _generate_html(self, data: Dict) -> str:
        """Generate complete HTML"""
        metrics = data['metrics']
        
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetLife Test Monitoring Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    <style>
        {self._get_professional_css()}
    </style>
</head>
<body>
    <div class="dashboard">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="logo">
                    <i class="fas fa-chart-line"></i>
                    <span>MetLife QA</span>
                </div>
            </div>
            <nav class="sidebar-nav">
                <a href="#overview" class="nav-item active">
                    <i class="fas fa-home"></i>
                    <span>Overview</span>
                </a>
                <a href="#metrics" class="nav-item">
                    <i class="fas fa-chart-bar"></i>
                    <span>Metrics</span>
                </a>
                <a href="#suites" class="nav-item">
                    <i class="fas fa-layer-group"></i>
                    <span>Test Suites</span>
                </a>
                <a href="#tests" class="nav-item">
                    <i class="fas fa-list-check"></i>
                    <span>Test Cases</span>
                </a>
                <a href="#insights" class="nav-item">
                    <i class="fas fa-lightbulb"></i>
                    <span>Insights</span>
                </a>
            </nav>
            <div class="sidebar-footer">
                <div class="status-indicator">
                    <span class="status-dot {'success' if metrics.system_health >= 80 else 'warning' if metrics.system_health >= 60 else 'error'}"></span>
                    <span>System {'Healthy' if metrics.system_health >= 80 else 'Warning' if metrics.system_health >= 60 else 'Critical'}</span>
                </div>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Top Bar -->
            <header class="top-bar">
                <div class="top-bar-left">
                    <h1>Test Monitoring Dashboard</h1>
                    <span class="breadcrumb">Home / Overview</span>
                </div>
                <div class="top-bar-right">
                    <div class="last-updated">
                        <i class="fas fa-clock"></i>
                        <span>Last updated: <span id="currentTime"></span></span>
                    </div>
                    <button class="btn-icon" onclick="location.reload()">
                        <i class="fas fa-sync-alt"></i>
                    </button>
                    <button class="btn-icon" id="themeToggle">
                        <i class="fas fa-moon"></i>
                    </button>
                </div>
            </header>

            <!-- Content Area -->
            <div class="content-area">
                <!-- Key Metrics Cards -->
                <section class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-header">
                            <span class="metric-label">Total Tests</span>
                            <i class="fas fa-list-check metric-icon"></i>
                        </div>
                        <div class="metric-value">{metrics.total_tests:,}</div>
                        <div class="metric-footer">
                            <span class="metric-change positive">
                                <i class="fas fa-arrow-up"></i> Active
                            </span>
                        </div>
                    </div>

                    <div class="metric-card success">
                        <div class="metric-header">
                            <span class="metric-label">Pass Rate</span>
                            <i class="fas fa-check-circle metric-icon"></i>
                        </div>
                        <div class="metric-value">{metrics.pass_rate:.1f}%</div>
                        <div class="metric-footer">
                            <span class="metric-change {'positive' if metrics.pass_rate >= 90 else 'negative'}">
                                {metrics.passed_tests} passed / {metrics.failed_tests} failed
                            </span>
                        </div>
                    </div>

                    <div class="metric-card info">
                        <div class="metric-header">
                            <span class="metric-label">Avg Execution Time</span>
                            <i class="fas fa-clock metric-icon"></i>
                        </div>
                        <div class="metric-value">{self._format_duration(metrics.avg_execution_time)}</div>
                        <div class="metric-footer">
                            <span class="metric-change">
                                Total: {self._format_duration(metrics.total_execution_time)}
                            </span>
                        </div>
                    </div>

                    <div class="metric-card warning">
                        <div class="metric-header">
                            <span class="metric-label">System Health</span>
                            <i class="fas fa-heartbeat metric-icon"></i>
                        </div>
                        <div class="metric-value">{metrics.system_health:.0f}%</div>
                        <div class="metric-footer">
                            <span class="metric-change {'positive' if metrics.system_health >= 80 else 'negative'}">
                                <i class="fas fa-{'arrow-up' if metrics.system_health >= 80 else 'arrow-down'}"></i>
                                {'Excellent' if metrics.system_health >= 90 else 'Good' if metrics.system_health >= 80 else 'Needs Attention'}
                            </span>
                        </div>
                    </div>
                </section>

                <!-- Charts Section -->
                <section class="charts-section">
                    <div class="chart-card">
                        <div class="card-header">
                            <h3>Test Results Distribution</h3>
                            <div class="card-actions">
                                <button class="btn-icon-sm"><i class="fas fa-expand"></i></button>
                            </div>
                        </div>
                        <div class="chart-container">
                            <canvas id="statusChart"></canvas>
                        </div>
                    </div>

                    <div class="chart-card">
                        <div class="card-header">
                            <h3>Execution Time Distribution</h3>
                            <div class="card-actions">
                                <button class="btn-icon-sm"><i class="fas fa-expand"></i></button>
                            </div>
                        </div>
                        <div class="chart-container">
                            <canvas id="timeChart"></canvas>
                        </div>
                    </div>

                    <div class="chart-card wide">
                        <div class="card-header">
                            <h3>Suite Performance Overview</h3>
                            <div class="card-actions">
                                <button class="btn-icon-sm"><i class="fas fa-expand"></i></button>
                            </div>
                        </div>
                        <div class="chart-container">
                            <canvas id="suiteChart"></canvas>
                        </div>
                    </div>
                </section>

                <!-- Insights Section -->
                <section class="insights-section">
                    <h2>Actionable Insights</h2>
                    <div class="insights-grid">
                        {self._generate_insights_html(data['insights'])}
                    </div>
                </section>

                <!-- Test Suites Table -->
                <section class="table-section">
                    <div class="table-header">
                        <h2>Test Suites</h2>
                        <div class="table-controls">
                            <div class="search-box">
                                <i class="fas fa-search"></i>
                                <input type="text" placeholder="Search suites..." id="suiteSearch">
                            </div>
                            <button class="btn-secondary">
                                <i class="fas fa-filter"></i> Filter
                            </button>
                            <button class="btn-secondary">
                                <i class="fas fa-download"></i> Export
                            </button>
                        </div>
                    </div>
                    <div class="table-container">
                        {self._generate_suites_table(data['suites'])}
                    </div>
                </section>

                <!-- Test Cases Table -->
                <section class="table-section">
                    <div class="table-header">
                        <h2>Recent Test Executions</h2>
                        <div class="table-controls">
                            <div class="search-box">
                                <i class="fas fa-search"></i>
                                <input type="text" placeholder="Search tests..." id="testSearch">
                            </div>
                            <select class="select-filter" id="statusFilter">
                                <option value="">All Status</option>
                                <option value="PASS">Passed</option>
                                <option value="FAIL">Failed</option>
                            </select>
                        </div>
                    </div>
                    <div class="table-container">
                        {self._generate_tests_table(data['tests'])}
                    </div>
                </section>
            </div>
        </main>
    </div>

    <script>
        {self._get_professional_javascript(data)}
    </script>
</body>
</html>"""
    
    def _get_professional_css(self) -> str:
        """Professional CSS styling"""
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-color: #2563eb;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --error-color: #ef4444;
            --info-color: #3b82f6;
            
            --bg-primary: #ffffff;
            --bg-secondary: #f9fafb;
            --bg-tertiary: #f3f4f6;
            
            --text-primary: #111827;
            --text-secondary: #6b7280;
            --text-tertiary: #9ca3af;
            
            --border-color: #e5e7eb;
            --sidebar-bg: #1f2937;
            --sidebar-text: #d1d5db;
            
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        [data-theme="dark"] {
            --bg-primary: #111827;
            --bg-secondary: #1f2937;
            --bg-tertiary: #374151;
            --text-primary: #f9fafb;
            --text-secondary: #d1d5db;
            --text-tertiary: #9ca3af;
            --border-color: #374151;
            --sidebar-bg: #0f172a;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg-secondary);
            color: var(--text-primary);
            line-height: 1.5;
        }

        .dashboard {
            display: flex;
            min-height: 100vh;
        }

        /* Sidebar */
        .sidebar {
            width: 260px;
            background: var(--sidebar-bg);
            color: var(--sidebar-text);
            display: flex;
            flex-direction: column;
            position: fixed;
            height: 100vh;
            z-index: 100;
        }

        .sidebar-header {
            padding: 1.5rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.25rem;
            font-weight: 600;
            color: white;
        }

        .logo i {
            color: var(--primary-color);
            font-size: 1.5rem;
        }

        .sidebar-nav {
            flex: 1;
            padding: 1rem 0;
        }

        .nav-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem 1.5rem;
            color: var(--sidebar-text);
            text-decoration: none;
            transition: all 0.2s;
            border-left: 3px solid transparent;
        }

        .nav-item:hover {
            background: rgba(255, 255, 255, 0.05);
            color: white;
        }

        .nav-item.active {
            background: rgba(37, 99, 235, 0.1);
            border-left-color: var(--primary-color);
            color: white;
        }

        .nav-item i {
            width: 20px;
            text-align: center;
        }

        .sidebar-footer {
            padding: 1.5rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .status-indicator {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.875rem;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        .status-dot.success {
            background: var(--success-color);
        }

        .status-dot.warning {
            background: var(--warning-color);
        }

        .status-dot.error {
            background: var(--error-color);
        }

        /* Main Content */
        .main-content {
            flex: 1;
            margin-left: 260px;
            display: flex;
            flex-direction: column;
        }

        .top-bar {
            background: var(--bg-primary);
            border-bottom: 1px solid var(--border-color);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 50;
        }

        .top-bar-left h1 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .breadcrumb {
            font-size: 0.875rem;
            color: var(--text-secondary);
        }

        .top-bar-right {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .last-updated {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.875rem;
            color: var(--text-secondary);
        }

        .btn-icon {
            width: 40px;
            height: 40px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background: var(--bg-primary);
            color: var(--text-secondary);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }

        .btn-icon:hover {
            background: var(--bg-tertiary);
            color: var(--text-primary);
        }

        .content-area {
            padding: 2rem;
            max-width: 1600px;
            margin: 0 auto;
            width: 100%;
        }

        /* Metrics Grid */
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .metric-card {
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s;
        }

        .metric-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }

        .metric-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .metric-label {
            font-size: 0.875rem;
            font-weight: 500;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .metric-icon {
            font-size: 1.5rem;
            opacity: 0.5;
        }

        .metric-card.success .metric-icon {
            color: var(--success-color);
        }

        .metric-card.info .metric-icon {
            color: var(--info-color);
        }

        .metric-card.warning .metric-icon {
            color: var(--warning-color);
        }

        .metric-value {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .metric-footer {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .metric-change {
            font-size: 0.875rem;
            display: flex;
            align-items: center;
            gap: 0.25rem;
        }

        .metric-change.positive {
            color: var(--success-color);
        }

        .metric-change.negative {
            color: var(--error-color);
        }

        /* Charts Section */
        .charts-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .chart-card {
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
        }

        .chart-card.wide {
            grid-column: 1 / -1;
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }

        .card-header h3 {
            font-size: 1.125rem;
            font-weight: 600;
        }

        .card-actions {
            display: flex;
            gap: 0.5rem;
        }

        .btn-icon-sm {
            width: 32px;
            height: 32px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background: transparent;
            color: var(--text-secondary);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }

        .btn-icon-sm:hover {
            background: var(--bg-tertiary);
        }

        .chart-container {
            position: relative;
            height: 300px;
        }

        /* Insights Section */
        .insights-section {
            margin-bottom: 2rem;
        }

        .insights-section h2 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
        }

        .insights-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1rem;
        }

        .insight-card {
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-left: 4px solid;
            border-radius: 8px;
            padding: 1.25rem;
        }

        .insight-card.success {
            border-left-color: var(--success-color);
        }

        .insight-card.warning {
            border-left-color: var(--warning-color);
        }

        .insight-card.info {
            border-left-color: var(--info-color);
        }

        .insight-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.75rem;
        }

        .insight-icon {
            width: 36px;
            height: 36px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.125rem;
        }

        .insight-card.success .insight-icon {
            background: rgba(16, 185, 129, 0.1);
            color: var(--success-color);
        }

        .insight-card.warning .insight-icon {
            background: rgba(245, 158, 11, 0.1);
            color: var(--warning-color);
        }

        .insight-card.info .insight-icon {
            background: rgba(59, 130, 246, 0.1);
            color: var(--info-color);
        }

        .insight-title {
            font-weight: 600;
            font-size: 1rem;
        }

        .insight-message {
            color: var(--text-secondary);
            font-size: 0.875rem;
            margin-bottom: 0.75rem;
        }

        .insight-action {
            font-size: 0.875rem;
            color: var(--primary-color);
            font-weight: 500;
        }

        /* Table Section */
        .table-section {
            background: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: var(--shadow-sm);
        }

        .table-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }

        .table-header h2 {
            font-size: 1.25rem;
            font-weight: 600;
        }

        .table-controls {
            display: flex;
            gap: 0.75rem;
        }

        .search-box {
            position: relative;
            display: flex;
            align-items: center;
        }

        .search-box i {
            position: absolute;
            left: 0.75rem;
            color: var(--text-tertiary);
        }

        .search-box input {
            padding: 0.5rem 0.75rem 0.5rem 2.5rem;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background: var(--bg-secondary);
            color: var(--text-primary);
            font-size: 0.875rem;
            min-width: 250px;
        }

        .btn-secondary {
            padding: 0.5rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background: var(--bg-primary);
            color: var(--text-primary);
            font-size: 0.875rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s;
        }

        .btn-secondary:hover {
            background: var(--bg-tertiary);
        }

        .select-filter {
            padding: 0.5rem 0.75rem;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background: var(--bg-secondary);
            color: var(--text-primary);
            font-size: 0.875rem;
            cursor: pointer;
        }

        .table-container {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            text-align: left;
            padding: 0.75rem;
            font-size: 0.875rem;
            font-weight: 600;
            color: var(--text-secondary);
            border-bottom: 2px solid var(--border-color);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        td {
            padding: 1rem 0.75rem;
            border-bottom: 1px solid var(--border-color);
            font-size: 0.875rem;
        }

        tr:hover {
            background: var(--bg-secondary);
        }

        .status-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }

        .status-badge.pass {
            background: rgba(16, 185, 129, 0.1);
            color: var(--success-color);
        }

        .status-badge.fail {
            background: rgba(239, 68, 68, 0.1);
            color: var(--error-color);
        }

        .progress-bar {
            width: 100px;
            height: 8px;
            background: var(--bg-tertiary);
            border-radius: 4px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: var(--success-color);
            transition: width 0.3s;
        }

        /* Animations */
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.5;
            }
        }

        /* Responsive */
        @media (max-width: 1024px) {
            .sidebar {
                transform: translateX(-100%);
            }

            .main-content {
                margin-left: 0;
            }

            .metrics-grid {
                grid-template-columns: 1fr;
            }

            .charts-section {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 768px) {
            .content-area {
                padding: 1rem;
            }

            .table-controls {
                flex-direction: column;
            }

            .search-box input {
                min-width: 100%;
            }
        }
        """
    
    def _generate_insights_html(self, insights: List[Dict]) -> str:
        """Generate insights HTML"""
        if not insights:
            return '<div class="insight-card info"><div class="insight-message">No insights available</div></div>'
        
        html = ""
        for insight in insights:
            icon_map = {
                'success': 'fa-check-circle',
                'warning': 'fa-exclamation-triangle',
                'info': 'fa-info-circle'
            }
            icon = icon_map.get(insight['type'], 'fa-info-circle')
            
            html += f"""
            <div class="insight-card {insight['type']}">
                <div class="insight-header">
                    <div class="insight-icon">
                        <i class="fas {icon}"></i>
                    </div>
                    <div class="insight-title">{insight['title']}</div>
                </div>
                <div class="insight-message">{insight['message']}</div>
                <div class="insight-action"><i class="fas fa-arrow-right"></i> {insight['action']}</div>
            </div>
            """
        
        return html
    
    def _generate_suites_table(self, suites: List[Dict]) -> str:
        """Generate suites table HTML"""
        html = """
        <table>
            <thead>
                <tr>
                    <th>Suite Name</th>
                    <th>Status</th>
                    <th>Tests</th>
                    <th>Pass Rate</th>
                    <th>Duration</th>
                </tr>
            </thead>
            <tbody>
        """
        
        for suite in suites[:20]:  # Show top 20 suites
            html += f"""
            <tr>
                <td><strong>{suite['name']}</strong></td>
                <td><span class="status-badge {'pass' if suite['status'] == 'PASS' else 'fail'}">{suite['status']}</span></td>
                <td>{suite['passed']} / {suite['total']}</td>
                <td>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {suite['pass_rate']}%"></div>
                    </div>
                    {suite['pass_rate']:.1f}%
                </td>
                <td>{self._format_duration(suite['elapsed_time'])}</td>
            </tr>
            """
        
        html += "</tbody></table>"
        return html
    
    def _generate_tests_table(self, tests: List[Dict]) -> str:
        """Generate tests table HTML"""
        html = """
        <table id="testsTable">
            <thead>
                <tr>
                    <th>Test Name</th>
                    <th>Suite</th>
                    <th>Status</th>
                    <th>Duration</th>
                    <th>Tags</th>
                </tr>
            </thead>
            <tbody>
        """
        
        for test in tests[:50]:  # Show top 50 tests
            tags_html = ' '.join([f'<span class="status-badge" style="background: rgba(37, 99, 235, 0.1); color: var(--primary-color);">{tag}</span>' 
                                 for tag in test['tags'][:3]])
            
            html += f"""
            <tr data-status="{test['status']}">
                <td><strong>{test['name']}</strong></td>
                <td>{test['suite']}</td>
                <td><span class="status-badge {'pass' if test['status'] == 'PASS' else 'fail'}">{test['status']}</span></td>
                <td>{self._format_duration(test['elapsed_time'])}</td>
                <td>{tags_html}</td>
            </tr>
            """
        
        html += "</tbody></table>"
        return html
    
    def _get_professional_javascript(self, data: Dict) -> str:
        """Professional JavaScript"""
        charts = data['charts']
        
        return f"""
        // Update clock
        function updateClock() {{
            const now = new Date();
            document.getElementById('currentTime').textContent = now.toLocaleString();
        }}
        setInterval(updateClock, 1000);
        updateClock();

        // Theme toggle
        const themeToggle = document.getElementById('themeToggle');
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.body.setAttribute('data-theme', savedTheme);
        
        themeToggle.addEventListener('click', () => {{
            const current = document.body.getAttribute('data-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';
            document.body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            themeToggle.querySelector('i').className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
        }});

        // Chart.js defaults
        Chart.defaults.font.family = 'Inter, sans-serif';
        Chart.defaults.color = '#6b7280';

        // Status Distribution Chart
        new Chart(document.getElementById('statusChart'), {{
            type: 'doughnut',
            data: {{
                labels: {json.dumps(list(charts['status_distribution'].keys()))},
                datasets: [{{
                    data: {json.dumps(list(charts['status_distribution'].values()))},
                    backgroundColor: ['#10b981', '#ef4444', '#f59e0b'],
                    borderWidth: 0
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom',
                        labels: {{
                            padding: 15,
                            usePointStyle: true
                        }}
                    }}
                }}
            }}
        }});

        // Time Distribution Chart
        new Chart(document.getElementById('timeChart'), {{
            type: 'bar',
            data: {{
                labels: {json.dumps(list(charts['time_distribution'].keys()))},
                datasets: [{{
                    label: 'Tests',
                    data: {json.dumps(list(charts['time_distribution'].values()))},
                    backgroundColor: '#3b82f6',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        display: false
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        grid: {{
                            color: '#e5e7eb'
                        }}
                    }},
                    x: {{
                        grid: {{
                            display: false
                        }}
                    }}
                }}
            }}
        }});

        // Suite Performance Chart
        const suiteData = {json.dumps(charts['suite_performance'])};
        new Chart(document.getElementById('suiteChart'), {{
            type: 'bar',
            data: {{
                labels: suiteData.map(s => s[0]),
                datasets: [{{
                    label: 'Duration (s)',
                    data: suiteData.map(s => s[1]),
                    backgroundColor: '#2563eb',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        display: false
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        grid: {{
                            color: '#e5e7eb'
                        }}
                    }},
                    x: {{
                        grid: {{
                            display: false
                        }}
                    }}
                }}
            }}
        }});

        // Search and filter functionality
        document.getElementById('testSearch').addEventListener('input', function() {{
            const searchTerm = this.value.toLowerCase();
            const rows = document.querySelectorAll('#testsTable tbody tr');
            rows.forEach(row => {{
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            }});
        }});

        document.getElementById('statusFilter').addEventListener('change', function() {{
            const status = this.value;
            const rows = document.querySelectorAll('#testsTable tbody tr');
            rows.forEach(row => {{
                if (!status || row.dataset.status === status) {{
                    row.style.display = '';
                }} else {{
                    row.style.display = 'none';
                }}
            }});
        }});

        // Navigation
        document.querySelectorAll('.nav-item').forEach(item => {{
            item.addEventListener('click', function(e) {{
                e.preventDefault();
                document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
                this.classList.add('active');
            }});
        }});
        """
    
    def _format_duration(self, seconds: float) -> str:
        """Format duration"""
        if seconds < 1:
            return f"{int(seconds * 1000)}ms"
        elif seconds < 60:
            return f"{seconds:.1f}s"
        else:
            minutes = int(seconds // 60)
            secs = seconds % 60
            return f"{minutes}m {secs:.0f}s"

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Generate Professional Test Monitoring Dashboard')
    parser.add_argument('--root-dir', '-r', default='.', help='Root directory to scan')
    parser.add_argument('--output', '-o', default='professional_dashboard.html', help='Output file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        # Parse data
        parser_obj = ProfessionalDashboardParser()
        data = parser_obj.parse_all_xml_files(args.root_dir)
        
        # Generate dashboard
        generator = ProfessionalDashboardGenerator()
        output_path = generator.generate(data, args.output)
        
        logger.info(f"✅ Professional dashboard generated: {output_path}")
        logger.info(f"📊 Metrics: {data['metrics'].total_tests} tests, {data['metrics'].pass_rate:.1f}% pass rate")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

