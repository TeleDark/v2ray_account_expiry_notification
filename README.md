# V2ray Account Expiry Notification Telegram Bot

This Telegram bot is designed to notify the admin whenever a customer's VPN account expires. The bot automatically sends a message to the admin, ensuring timely updates on the status of customer accounts.

## Install & Upgrade

```
bash <(curl -Ls https://raw.githubusercontent.com/TeleDark/2ray_account_expiry_notification/main/install.sh)
```
3. **Configure the bot**:
   - Get your bot token from [BotFather](https://t.me/BotFather) on Telegram.
   - Get your chat ID from [userinfobot](https://t.me/userinfobot) on Telegram.
   - Update the `config.yaml` file with your bot token and admin chat ID.

4. **Run the bot**:
    ```bash
    reboot
    ```

## Usage

- The bot will monitor the v2ray accounts and send an automatic notification to the admin when an account expires.

## Contributing

If you have any suggestions or improvements, please create a pull request or open an issue.

## License

This project is licensed under the GNU General Public License v3.0.

---

Feel free to adjust the instructions based on your actual implementation details.
