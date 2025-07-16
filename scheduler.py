#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定时执行脚本

这个脚本会根据配置的时间间隔自动执行网页截图任务。
"""

import time
import os
import signal
import sys
from datetime import datetime, timedelta
from web_screenshot import WebScreenshot
from config import *


class Scheduler:
    def __init__(self):
        self.execution_count = 0
        self.success_count = 0
        self.failed_count = 0
        self.start_time = None
        self.running = True

        # 注册信号处理器，支持优雅退出
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    def signal_handler(self, signum, frame):
        """信号处理器，用于优雅退出"""
        print(f"\n收到退出信号 {signum}，正在优雅退出...")
        self.running = False
        self.show_final_stats()
        sys.exit(0)

    def show_stats(self):
        """显示执行统计"""
        if not SHOW_STATS:
            return

        if self.start_time:
            elapsed_time = datetime.now() - self.start_time
            elapsed_minutes = elapsed_time.total_seconds() / 60

            print("\n" + "="*50)
            print("📊 执行统计")
            print("="*50)
            print(f"总执行次数: {self.execution_count}")
            print(f"成功次数: {self.success_count}")
            print(f"失败次数: {self.failed_count}")
            print(
                f"成功率: {(self.success_count/self.execution_count*100):.1f}%" if self.execution_count > 0 else "成功率: 0%")
            print(f"运行时间: {elapsed_minutes:.1f} 分钟")
            print(
                f"平均间隔: {elapsed_minutes/self.execution_count:.1f} 分钟/次" if self.execution_count > 0 else "平均间隔: 0 分钟/次")
            print("="*50)

    def show_final_stats(self):
        """显示最终统计"""
        print("\n" + "="*50)
        print("🏁 最终执行统计")
        print("="*50)
        print(f"总执行次数: {self.execution_count}")
        print(f"成功次数: {self.success_count}")
        print(f"失败次数: {self.failed_count}")
        if self.execution_count > 0:
            print(f"成功率: {(self.success_count/self.execution_count*100):.1f}%")
        if self.start_time:
            elapsed_time = datetime.now() - self.start_time
            elapsed_minutes = elapsed_time.total_seconds() / 60
            print(f"总运行时间: {elapsed_minutes:.1f} 分钟")
        print("="*50)

    def execute_task(self):
        """执行一次截图任务"""
        try:
            print(f"\n🔄 开始第 {self.execution_count + 1} 次执行...")
            print(f"⏰ 执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            # 创建自动化实例
            automation = WebScreenshot()

            # 运行自动化流程
            result = automation.run_automation(TARGET_URL)

            if result:
                self.success_count += 1
                print(f"✅ 第 {self.execution_count + 1} 次执行成功！截图保存在: {result}")
            else:
                self.failed_count += 1
                print(f"❌ 第 {self.execution_count + 1} 次执行失败！")

        except Exception as e:
            self.failed_count += 1
            print(f"❌ 第 {self.execution_count + 1} 次执行出错: {e}")

        self.execution_count += 1

    def run(self):
        """运行定时器"""
        print("="*60)
        print("🕐 定时执行器启动")
        print("="*60)
        print(f"目标网页: {TARGET_URL}")
        print(f"执行间隔: {SCHEDULE_INTERVAL_MINUTES} 分钟")
        print(f"最大执行次数: {'无限' if MAX_EXECUTIONS == 0 else MAX_EXECUTIONS}")
        print(f"无头模式: {'启用' if HEADLESS_MODE else '禁用'}")
        print("="*60)
        print("按 Ctrl+C 停止执行")
        print("="*60)

        self.start_time = datetime.now()

        # 立即执行一次
        self.execute_task()

        # 定时执行
        while self.running:
            # 检查是否达到最大执行次数
            if MAX_EXECUTIONS > 0 and self.execution_count >= MAX_EXECUTIONS:
                print(f"\n🎯 已达到最大执行次数 {MAX_EXECUTIONS}，停止执行")
                break

            # 显示统计信息
            self.show_stats()

            # 计算下次执行时间
            next_execution = datetime.now() + timedelta(minutes=SCHEDULE_INTERVAL_MINUTES)
            print(
                f"\n⏳ 下次执行时间: {next_execution.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"⏰ 等待 {SCHEDULE_INTERVAL_MINUTES} 分钟...")

            # 等待到下次执行时间
            try:
                time.sleep(SCHEDULE_INTERVAL_MINUTES * 60)
            except KeyboardInterrupt:
                print("\n收到中断信号，正在退出...")
                break

            # 执行任务
            self.execute_task()

        # 显示最终统计
        self.show_final_stats()


def main():
    """主函数"""
    if not ENABLE_SCHEDULER:
        print("❌ 定时执行功能未启用！")
        print("请在 config.py 中设置 ENABLE_SCHEDULER = True")
        return

    if SCHEDULE_INTERVAL_MINUTES <= 0:
        print("❌ 执行间隔时间必须大于0！")
        print("请在 config.py 中设置 SCHEDULE_INTERVAL_MINUTES > 0")
        return

    # 创建并运行定时器
    scheduler = Scheduler()
    scheduler.run()


if __name__ == "__main__":
    main()
