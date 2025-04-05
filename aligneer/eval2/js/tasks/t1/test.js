import {PolishVehicleRegistrationCertificateDecoder} from './polish-vehicle-registration-certificate-decoder'
import {PolishVehicleRegistrationCertificateFuel} from './polish-vehicle-registration-certificate-fields'

describe('PolishVehicleRegistrationCertificateDecoder', () => {
  it('should decode new format', () => {
    const decoder = new PolishVehicleRegistrationCertificateDecoder(
      'AwMDAgICAxfjB8eHh8fERyw6ljaeSBrb211bmlrYWN5bmEgeSBzdOSCc3kgcm9qw7FuaSB3IEx1YmxpbmllfERyw6ljaeSBrb211bmlrYWN5bmEgeSBzdOSCc3kgcm9qw7FuaSB3IEx1YmxpbmllfERyw6ljaeSBrb211bmlrYWN5bmEgeSBzdOSCc3kgcm9qw7FuaSB3IEx1YmxpbmllfERyw6ljaeSBrb211bmlrYWN5bmEgeSBzdOSCc3kgcm9qw7FuaSB3IEx1YmxpbmllfHwxfEwyNTk4NnxPw5PTfFRPQkxPfE1PVF9QUk9GXFBBTlRBfEZPVFV8fFRPMzk5OTk5OTk5OTk5fE5ldyBGb3JtYXQgMjAyMi0wMS0wMXx8fEpvaG4gRG9lfEpvaG58RG9lfHx8OTk5OTk5OTk5OTl8fDIwMjItMDEtMDF8MjAyMi0wMS0wMXx8fEpvaG4gRG9lfEpvaG4gfERvZXx8fDEyMzQ1Njc4OTB8fDIwLTAxLTAxfDIwMjItMDEtMDF8MjAyMi0wMS0wMXx8fDEwMDB8MTAwMHwwfDEwMDB8fE1JX3YwMXx8fDEwfHwwfHwxfDIwMjItMDEtMDF8MXwwfE1PVF9DQVJ8fDE5ODktMDEtMDF8MTAwfHwwfHwxfHwxfHwwfHwwfHwwfHwwfHwwfHwxfHwwfHww'
    )

    expect(decoder.data.format.value).toBe('XX')
    expect(decoder.data.markaPojazdu.value).toBe('TOYOTA')
    expect(decoder.data.dataPierwszejRejestracjiPojazdu.value).toBe('1989-01-01')
    expect((decoder.data.rodzajPaliwa as PolishVehicleRegistrationCertificateFuel).valueDescription).toBe('benzyna')

    expect(decoder.data.organWydajacy.value).toEqual([
      'Dolnośląski komisarz sb i wyższych rang w Lublinie',
      'Dolnośląski komisarz sb i wyższych rang w Lublinie',
      'Dolnośląski komisarz sb i wyższych rang w Lublinie',
      'Dolnośląski komisarz sb i wyższych rang w Lublinie',
    ])

  })

  it('should decode old format', () => {
      const b64Encoded = 'AwMDAwICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgMHxEQnxBMDEyMzQ1Njc4fE9QRUxfQVNDSVl8fE9QRUxfQVNDSVl8fHwxfFRlc3R8fFRlc3R8fFRlc3R8fDEyMzQ1Njc4OTB8fFRlc3R8fHwxfHwxfHwxfHwxfDIwfDIwfDIwfDIwfDIwfDIwfDIw'
      const decoder = new PolishVehicleRegistrationCertificateDecoder(b64Encoded);

      expect(decoder.data.format.value).toBe('DB')
      expect(decoder.data.markaPojazdu.value).toBe('OPEL_ASCII')
      expect(decoder.data.numerIdentyfikacyjnyPojazdu.value).toBe('Test')
  })


  it('should handle invalid base64 input', () => {
    expect(() => new PolishVehicleRegistrationCertificateDecoder('invalid base64')).toThrow()
  });

  it('should handle decompression errors', () => {
    // Create a mock Buffer that simulates a decompression error
    const mockBuffer = {
      readUInt32LE: jest.fn(),
      slice: jest.fn().mockReturnValue(Buffer.from([])), // Empty buffer will cause decompression to fail
    } as unknown as Buffer;

    jest.spyOn(Buffer, 'from').mockReturnValue(mockBuffer);

    expect(() => new PolishVehicleRegistrationCertificateDecoder('some base64')).toThrow();

    // Restore the original Buffer.from
    jest.restoreAllMocks();
  });
});