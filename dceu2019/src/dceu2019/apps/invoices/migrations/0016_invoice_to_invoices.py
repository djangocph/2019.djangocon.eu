# Generated by Django 2.1.4 on 2019-03-18 21:32

from django.db import migrations


def single_to_multiple_invoices(apps, schema_editor):
    """
    We used to have a single invoice per ticket, now we can have several
    invoices because we cannot tell which order_line in Ticketbutler data
    belongs to which ticket, and we are not able to create combined invoices
    with our current API iteration structure... unless someone stays up for
    some more nights :)
    """
    TicketbutlerTicket = apps.get_model('invoices', 'TicketbutlerTicket')
    for ticket in TicketbutlerTicket.objects.exclude(invoice=None):
        if not ticket.invoices.filter(id=ticket.invoice.id).exists():
            ticket.invoices.add(ticket.invoice)


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0015_auto_20190318_2131'),
    ]

    operations = [
        migrations.RunPython(single_to_multiple_invoices),
    ]